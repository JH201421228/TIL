import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def nCm(n, m):
    if m > n//2:
        return nCm(n, n-m)

    res = 1

    for v in range(n, n-m, -1):
        res *= v

    for v in range(1, m+1):
        res //= v

    return res


print(nCm(*list(map(int, input().split()))))