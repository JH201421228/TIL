import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def cal(alpha, beta, gamma):
    res = 0
    for idx in range(4):
        if alpha[idx] == beta[idx] and beta[idx] == gamma[idx]: continue
        else: res += 2

    return res


def solve(n):
    res = float("inf")

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                res = min(res, cal(mbtis[i], mbtis[j], mbtis[k]))

    return res


for _ in range(int(input())):
    N = int(input())

    mbtis = list(input().rstrip().split())

    if N > 32:
        print(0)
    else:
        print(solve(N))