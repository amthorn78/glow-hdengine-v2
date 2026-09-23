import sys
sys.dont_write_bytecode = True
def apply(path, edits, label=''):
    s = open(path, encoding='utf-8').read()
    for i, (old, new) in enumerate(edits):
        n = s.count(old)
        assert n == 1, (label or path, i, n, old[:120])
        s = s.replace(old, new)
    open(path, 'w', encoding='utf-8').write(s)
    return s
