import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
D = [[float("inf")] * N for _ in range(N)]

for _ in range(K):
    u, v = map(int, input().split())
    D[u-1][v-1], D[v-1][u-1] = 1, 1
    for i in range(N): D[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

for i in range(N):
    for j in range(i+1, N):
        if D[i][j] > 6:
            print("Big World!")
            exit(0)

print("Small World!")