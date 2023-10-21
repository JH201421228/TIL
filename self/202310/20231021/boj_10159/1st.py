import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
M = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if not graph[i][j] and graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# for inner in graph:
#     print(inner)

for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp += (graph[i][j] + graph[j][i])
    print((N-1)-temp)