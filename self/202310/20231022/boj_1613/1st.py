import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    start, end = map(int, input().split())
    graph[start][end] = 1
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if not graph[i][j] and graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for _ in range(int(input())):
    start, end = map(int, input().split())
    if graph[start][end]:
        print(-1)
    elif graph[end][start]:
        print(1)
    else:
        print(0)
