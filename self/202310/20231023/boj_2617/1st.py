import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if not graph[i][j] and graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# for inner in graph[1:]:
#     print(inner[1:])

mid = N//2 + 1
ans = 0
for i in range(1, N+1):
    front = 0
    back = 0
    for j in range(1, N+1):
        if graph[j][i]:
            front += 1
        if graph[i][j]:
            back += 1
    if front >= mid or back >= mid:
        ans += 1
print(ans)
