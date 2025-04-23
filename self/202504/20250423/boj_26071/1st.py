import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
screen = [list(input().rstrip()) for _ in range(N)]

max_i, min_i, max_j, min_j = -float("inf"), float("inf"), -float("inf"), float("inf")

cnt = 0

for i in range(N):
    for j in range(N):
        if screen[i][j] == 'G':
            cnt += 1
            max_i, min_i, max_j, min_j = max(max_i, i), min(min_i, i), max(max_j, j), min(min_j, j)

if cnt == 1: print(0)
elif max_i == min_i: print(min(max_j, N-1-min_j))
elif max_j == min_j: print(min(max_i, N-1-min_i))
else: print(min(max_i, N-1-min_i) + min(max_j, N-1-min_j))