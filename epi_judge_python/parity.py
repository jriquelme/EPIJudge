from test_framework import generic_test


def byte_parity(b: int) -> int:
    c = 0
    while b > 0:
        c += 1 & b
        b >>= 1
    return c % 2


def parity(x: int) -> int:
    c = 0
    cache = {}
    for _ in range(8):
        n = x & 255
        if n not in cache:
            cache[n] = byte_parity(n)
        c += cache[n]
        x >>= 8
    return c % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
