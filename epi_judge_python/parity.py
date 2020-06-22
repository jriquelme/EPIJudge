from test_framework import generic_test


def byte_parity(b: int) -> int:
    c = 0
    while b > 0:
        c ^= 1
        b &= b - 1
    return c


cache = []
for i in range(0, 2 ** 16 - 1):
    cache.append(byte_parity(i))


def parity(x: int) -> int:
    c = 0
    m = 2 ** 16 - 1
    for _ in range(4):
        n = x & m
        c ^= cache[n] & 1
        x >>= 16
    return c


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
