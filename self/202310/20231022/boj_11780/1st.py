import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def path_finder(i, j):
    if not visited[i][j]:
        return []

    n = visited[i][j]
    return path_finder(i, n) + [n] + path_finder(n, j)


N = int(input())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
visited = [[0] * (N+1) for _ in range(N+1)]
for _ in range(int(input())):
    start, end, cost = map(int, input().split())
    graph[start][end] = min(graph[start][end], cost)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][i] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                visited[i][j] = k

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0

for inner in graph[1:]:
    print(*inner[1:])
# for inner in visited[1:]:
#     print(inner[1:])
for i in range(1, N+1):
    for j in range(1, N+1):
        if not graph[i][j]:
            print(0)
        else:
            ans = [i] + path_finder(i, j) + [j]
            print(len(ans), *ans)