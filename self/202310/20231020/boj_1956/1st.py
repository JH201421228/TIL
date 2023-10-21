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
    if i == j:
        ans.append(graph[i][i])
real = min(ans)
if real == float('inf'):
    print(-1)
else:
    print(real)
