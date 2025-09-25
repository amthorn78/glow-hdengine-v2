import pathlib
from core.canon.validate import load_repo_canon, validate_counts, validate_ids, validate_degree

def test_repo_canon_counts_and_ids_and_degree():
    canon = load_repo_canon(pathlib.Path("."))
    issues = []
    issues += validate_counts(canon)
    issues += validate_ids(canon)
    issues += validate_degree(canon)
    # Expect no issues for these invariants in the repo canon
    assert issues == [], f"unexpected canon issues: {issues}"
