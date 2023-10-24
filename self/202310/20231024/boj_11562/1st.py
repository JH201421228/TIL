import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
fake = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(M):
    start, end, s = map(int, input().split())
    if s:
        graph[start][end] = graph[end][start] = 0
    else:
        graph[end][start] = 1
        graph[start][end] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for _ in range(int(input())):
    start, end = map(int, input().split())
    if start == end:
        print(0)
    else:
        print(graph[start][end])

# for inner in graph[1:]:
#     print(inner[1:])