\pset format unaligned
\pset tuples_only on
SELECT 'SCHEMA:' || nspname FROM pg_namespace WHERE nspname='hde';
SELECT 'TABLE:' || table_name || ' COLUMN:' || column_name || ' TYPE:' || data_type
FROM information_schema.columns WHERE table_schema='hde'
ORDER BY table_name, ordinal_position;
SELECT 'INDEX:' || schemaname || '.' || indexname || ' ON ' || tablename
FROM pg_indexes WHERE schemaname='hde'
ORDER BY tablename, indexname;
SELECT 'PARTITION:' || p.relname || ' -> ' || c.relname
FROM pg_inherits
JOIN pg_class p ON p.oid = pg_inherits.inhparent
JOIN pg_class c ON c.oid = pg_inherits.inhrelid
JOIN pg_namespace n ON n.oid = p.relnamespace
WHERE n.nspname='hde'
ORDER BY p.relname, c.relname;
