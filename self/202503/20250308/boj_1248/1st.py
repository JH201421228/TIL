import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def recursion(idx):
    if idx:
        for n in range(idx):
            if (matrix[n][idx-1] > 0 and G[n][idx-1] == '+') or (matrix[n][idx-1] < 0 and G[n][idx-1] == '-') or (not matrix[n][idx-1] and G[n][idx-1] == '0'):
                continue
            else:
                return

    if idx == N:
        print(*arr)
        exit(0)

    for n in range(-10, 11):
        arr[idx] = n
        matrix[idx][idx] = n

        for row in range(idx):
            matrix[row][idx] = matrix[row][idx-1] + n

        recursion(idx+1)

        for row in range(idx):
            matrix[row][idx] = 0

N = int(input())
characters = list(input().rstrip())

G = []
matrix = [[0] * N for _ in range(N)]
arr = [0] * N

idx = 0
for n in range(N):
    G.append([0] * n + characters[idx:idx+N-n])
    idx = idx+N-n

recursion(0)