import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(val, now, cnt):
    global ans

    if cnt == N and val < ans:
        ans = val
        return

    if val >= ans:
        return

    for next in range(N):
        if not visited[next]:
            visited[next] = 1
            dfs(val+graph[now][next], next, cnt+1)
            visited[next] = 0


N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or i == k or j == k:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# for inner in graph:
#     print(inner)
visited = [0] * N
visited[K] = 1
ans = float('inf')
dfs(0, K, 1)
print(ans)