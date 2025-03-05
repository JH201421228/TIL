import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve(n):

    ori = n
    res = 0
    pre = 0

    while n:
        if T[n]:
           pre = n

        res += T[n]
        n //= 2

    if pre:
        return pre
    else:
        T[ori] = 1
        return 0


N, Q = map(int, input().split())

T = [0] * (4*N+1)

for _ in range(Q):
    print(solve(int(input())))