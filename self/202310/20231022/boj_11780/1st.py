import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
visited = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(int(input())):
    start, end, cost = map(int, input().split())
    graph[start][end] = min(graph[start][end], cost)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][i] = 0
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for inner in graph[1:]:
    print(*inner[1:])
# for inner in visited:
#     print(inner)
print(visited[1][1])