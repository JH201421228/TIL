import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1
# print(graph)
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if not graph[i][j] and graph[i][k] and graph[k][j]:
                graph[i][j] = 1
# print(graph)
ans = 0
for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp += (graph[i][j] + graph[j][i])
    if temp == N-1:
        ans += 1
print(ans)
