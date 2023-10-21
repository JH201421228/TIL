import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


V, E = map(int, input().split())
graph = [[float('inf')] * (V+1) for _ in range(V+1)]
for _ in range(E):
    start, end, dist = map(int, input().split())
    graph[start][end] = dist
# print(graph)
ans = []
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

output = float('inf')
for i in range(1, V+1):
    output = min(output, graph[i][i])

if output == float('inf'):
    print(-1)
else:
    print(output)