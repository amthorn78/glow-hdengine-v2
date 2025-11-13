#!/usr/bin/env python3
import json
import re
from pathlib import Path

DISCOVERY_DIR = Path('artifacts/db_discovery/20251113')
FILES = {
    'schemas': DISCOVERY_DIR / '00_schemas_and_search_path.txt',
    'tables': DISCOVERY_DIR / '01_tables_by_schema.txt',
    'columns': DISCOVERY_DIR / '02_columns.txt',
    'constraints': DISCOVERY_DIR / '03_primary_and_unique_keys.txt',
    'foreign_keys': DISCOVERY_DIR / '04_foreign_keys.txt',
    'indexes': DISCOVERY_DIR / '05_indexes.txt',
    'views': DISCOVERY_DIR / '06_views.txt',
    'schema_dump': DISCOVERY_DIR / 'postgres_schema_only.sql',
}


def parse_table_file(path: Path, expected_cols: int | None = None, header_skip_prefixes: list[str] | None = None):
    rows: list[list[str]] = []
    if not path.exists():
        return rows
    for raw_line in path.read_text().splitlines():
        if '|' not in raw_line:
            continue
        if '+-' in raw_line:
            continue
        stripped = raw_line.strip()
        if header_skip_prefixes and any(stripped.startswith(prefix) for prefix in header_skip_prefixes):
            continue
        parts = [part.strip() for part in raw_line.split('|')]
        if expected_cols and len(parts) < expected_cols:
            continue
        rows.append(parts)
    return rows


def load_inventory() -> dict:
    schema_rows = parse_table_file(FILES['schemas'], expected_cols=4, header_skip_prefixes=['Name'])
    schemas: dict[str, dict] = {}
    for row in schema_rows:
        name = row[0]
        if not name:
            continue
        schemas[name] = {
            'name': name,
            'in_search_path': False,
            'tables': [],
            'views': [],
        }

    search_path: list[str] = []
    schema_lines = FILES['schemas'].read_text().splitlines()
    for idx, line in enumerate(schema_lines):
        if line.strip() == 'search_path':
            for candidate in schema_lines[idx + 1:]:
                normalized = candidate.strip()
                if not normalized or normalized.startswith('(') or set(normalized) == {'-'}:
                    continue
                search_path = [part.strip() for part in normalized.split(',') if part.strip()]
                break
            break
    for schema in schemas.values():
        schema['in_search_path'] = schema['name'] in search_path

    table_rows = parse_table_file(FILES['tables'], expected_cols=3, header_skip_prefixes=['table_schema'])
    for table_schema, table_name, table_type in table_rows:
        schema_entry = schemas.get(table_schema)
        if not schema_entry:
            schema_entry = schemas.setdefault(table_schema, {
                'name': table_schema,
                'in_search_path': table_schema in search_path,
                'tables': [],
                'views': [],
            })
        schema_entry['tables'].append({
            'name': table_name,
            'table_type': table_type if table_type else 'OTHER',
            'columns': [],
            'primary_key': {'constraint_name': None, 'columns': []},
            'unique_constraints': [],
            'foreign_keys': [],
            'indexes': [],
            'is_candidate_for_bodygraph': False,
        })

    def get_table(schema_name: str, table_name: str) -> dict | None:
        schema_entry = schemas.get(schema_name)
        if not schema_entry:
            return None
        for table in schema_entry['tables']:
            if table['name'] == table_name:
                return table
        return None

    column_rows = parse_table_file(FILES['columns'], expected_cols=7, header_skip_prefixes=['table_schema'])
    for row in column_rows:
        table_schema, table_name, column_name, ordinal_position, data_type, is_nullable, column_default = row[:7]
        if not table_schema or table_schema.lower() == 'table_schema':
            continue
        table = get_table(table_schema, table_name)
        if not table:
            continue
        try:
            ordinal = int(ordinal_position)
        except ValueError:
            ordinal = None
        table['columns'].append({
            'name': column_name,
            'ordinal_position': ordinal,
            'data_type': data_type,
            'is_nullable': (is_nullable.upper() == 'YES'),
            'column_default': column_default if column_default else None,
        })

    for schema_entry in schemas.values():
        for table in schema_entry['tables']:
            table['columns'].sort(key=lambda col: (col['ordinal_position'] is None, col['ordinal_position']))

    pk_constraints: dict[tuple[str, str], dict] = {}
    unique_constraints: dict[tuple[str, str], list[dict]] = {}
    constraint_rows = parse_table_file(FILES['constraints'], expected_cols=5, header_skip_prefixes=['constraint_type'])
    for row in constraint_rows:
        constraint_type, constraint_name, table_schema, table_name, columns = row[:5]
        cols = [col.strip() for col in columns.split(',') if col.strip()]
        key = (table_schema, table_name)
        if constraint_type.upper() == 'PRIMARY KEY':
            pk_constraints[key] = {
                'constraint_name': constraint_name,
                'columns': cols,
            }
        elif constraint_type.upper() == 'UNIQUE':
            unique_constraints.setdefault(key, []).append({
                'constraint_name': constraint_name,
                'columns': cols,
            })

    for (schema_name, table_name), pk in pk_constraints.items():
        table = get_table(schema_name, table_name)
        if table:
            table['primary_key'] = pk

    for (schema_name, table_name), uniques in unique_constraints.items():
        table = get_table(schema_name, table_name)
        if table:
            table['unique_constraints'] = uniques

    relationships_fks: list[dict] = []
    fk_rows = parse_table_file(FILES['foreign_keys'], expected_cols=8, header_skip_prefixes=['constraint_name'])
    for row in fk_rows:
        if len(row) < 8:
            continue
        constraint_name = row[0]
        fk_schema = row[1]
        fk_table = row[2]
        fk_columns = row[3]
        pk_schema = row[5]
        pk_table = row[6]
        pk_columns = row[7]
        fk_cols = [col.strip() for col in fk_columns.split(',') if col.strip()]
        pk_cols = [col.strip() for col in pk_columns.split(',') if col.strip()]
        fk_entry = {
            'constraint_name': constraint_name,
            'fk_columns': fk_cols,
            'pk_schema': pk_schema,
            'pk_table': pk_table,
            'pk_columns': pk_cols,
        }
        table = get_table(fk_schema, fk_table)
        if table:
            table['foreign_keys'].append(fk_entry)
        relationships_fks.append({
            'constraint_name': constraint_name,
            'fk_schema': fk_schema,
            'fk_table': fk_table,
            'pk_schema': pk_schema,
            'pk_table': pk_table,
            'fk_columns': fk_cols,
            'pk_columns': pk_cols,
        })

    schema_sql = FILES['schema_dump'].read_text()
    fk_pattern = re.compile(
        r"ALTER TABLE ONLY\s+([^.]+)\.([\w\"]+)\s+ADD CONSTRAINT\s+([\w\"]+)\s+FOREIGN KEY\s*\(([^)]+)\)\s+REFERENCES\s+([^.]+)\.([\w\"]+)\(([^)]+)\);",
        re.IGNORECASE,
    )
    for match in fk_pattern.finditer(schema_sql):
        fk_schema, fk_table, constraint_name, fk_columns, pk_schema, pk_table, pk_columns = match.groups()
        fk_table = fk_table.strip('"')
        constraint_name = constraint_name.strip('"')
        pk_table = pk_table.strip('"')
        fk_cols = [col.strip().strip('"') for col in fk_columns.split(',') if col.strip()]
        pk_cols = [col.strip().strip('"') for col in pk_columns.split(',') if col.strip()]
        fk_entry = {
            'constraint_name': constraint_name,
            'fk_columns': fk_cols,
            'pk_schema': pk_schema,
            'pk_table': pk_table,
            'pk_columns': pk_cols,
        }
        table = get_table(fk_schema, fk_table)
        if table and not any(existing['constraint_name'] == constraint_name for existing in table['foreign_keys']):
            table['foreign_keys'].append(fk_entry)
        if not any(existing['constraint_name'] == constraint_name for existing in relationships_fks):
            relationships_fks.append({
                'constraint_name': constraint_name,
                'fk_schema': fk_schema,
                'fk_table': fk_table,
                'pk_schema': pk_schema,
                'pk_table': pk_table,
                'fk_columns': fk_cols,
                'pk_columns': pk_cols,
            })

    index_rows = parse_table_file(FILES['indexes'], expected_cols=4, header_skip_prefixes=['schemaname'])
    for schemaname, tablename, indexname, indexdef in index_rows:
        table = get_table(schemaname, tablename)
        if table:
            table['indexes'].append({
                'index_name': indexname,
                'indexdef': indexdef,
            })

    view_rows = parse_table_file(FILES['views'], expected_cols=3, header_skip_prefixes=['table_schema'])
    for schema_name, view_name, view_definition in view_rows:
        schema_entry = schemas.get(schema_name)
        if not schema_entry:
            schema_entry = schemas.setdefault(schema_name, {
                'name': schema_name,
                'in_search_path': schema_name in search_path,
                'tables': [],
                'views': [],
            })
        schema_entry['views'].append({
            'name': view_name,
            'definition_snippet': view_definition[:200],
        })

    for schema_name, schema_entry in schemas.items():
        for table in schema_entry['tables']:
            table['is_candidate_for_bodygraph'] = schema_name == 'public'

    existing_bodygraph_like: list[str] = []
    user_tables: list[str] = []
    for schema_name, schema_entry in schemas.items():
        for table in schema_entry['tables']:
            full_name = f"{schema_name}.{table['name']}"
            if re.search(r'(bodygraph|bg_)', table['name'], re.IGNORECASE):
                existing_bodygraph_like.append(full_name)
            if 'user' in table['name']:
                user_tables.append(full_name)

    signals = {
        'existing_bodygraph_like_tables': sorted(existing_bodygraph_like),
        'user_tables': sorted(user_tables),
        'engine_like_schemas': sorted(name for name in schemas if name not in {'pg_catalog', 'information_schema', 'public'}),
    }

    schemas_list = []
    for schema_entry in schemas.values():
        schemas_list.append({
            'name': schema_entry['name'],
            'in_search_path': schema_entry['in_search_path'],
            'tables': sorted(schema_entry['tables'], key=lambda table: table['name']),
            'views': sorted(schema_entry['views'], key=lambda view: view['name']),
        })

    relationships = {
        'foreign_keys': sorted(
            relationships_fks,
            key=lambda fk: (fk['fk_schema'], fk['fk_table'], fk['constraint_name']),
        ),
    }

    return {
        'version': 'v1',
        'sources': {
            'discovery_dir': str(DISCOVERY_DIR),
            'schema_dump': str(FILES['schema_dump']),
        },
        'schemas': sorted(schemas_list, key=lambda schema: schema['name']),
        'relationships': relationships,
        'signals': signals,
    }


def main() -> None:
    inventory = load_inventory()
    output_path = Path('audit/db_plan/db_inventory.json')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(inventory, sort_keys=True, indent=2) + '\n')
    print(f"search_path: {', '.join(schema['name'] for schema in inventory['schemas'] if schema['in_search_path'])}")
    print(f"schemas: {len(inventory['schemas'])}")
    print(f"tables: {sum(len(schema['tables']) for schema in inventory['schemas'])}")
    print(f"foreign_keys: {len(inventory['relationships']['foreign_keys'])}")
    print(f"Wrote {output_path}")


if __name__ == '__main__':
    main()
