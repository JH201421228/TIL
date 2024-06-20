import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
MA, MI, MA_R, MI_R = [N] * (N+1), [1] * (N+1)
G = [set() for _ in range(N+1)]

for _ in range(M):
    temp = list(map(int, input().split()))

    if temp[0] == 1:

    else:
        pass