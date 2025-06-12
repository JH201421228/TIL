import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    H, D, K = map(int, input().split())
    damage = [int(input()) for _ in range(N)]

    status = [[float("inf")] * (N+1) for _ in range(2)]
    status[0][0] = 0

    for i in range(N):
        for 

    return


if __name__ == "__main__":
    solve()