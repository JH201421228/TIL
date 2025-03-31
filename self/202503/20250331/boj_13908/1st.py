import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve(N):
    res = 0

    for n in range(10**N):
        for c in arr:
            if c not in list(str(n).zfill(N)):
                break
        else:
            res += 1

    print(res)

    return

N, M = map(int, input().split())
arr = list(input().rstrip().split())

solve(N)