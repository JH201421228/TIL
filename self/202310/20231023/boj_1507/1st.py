import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
ans = 0
graph = [list(map(int, input().split())) for _ in range(N)]
prime_graph = [graph[i][:] for i in range(N)]
replica_graph = [[float('inf')] * N for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(i+1, N):
            if graph[i][k] and graph[k][j] and graph[i][j] == graph[i][k] + graph[k][j]:
                graph[i][j] = 0

for i in range(N):
    for j in range(i+1, N):
        if not graph[i][j]:
            continue
        replica_graph[i][j] = replica_graph[j][i] = graph[i][j]
        ans += graph[i][j]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            replica_graph[i][j] = min(replica_graph[i][j], replica_graph[i][k] + replica_graph[k][j])

for i in range(N):
    for j in range(i+1, N):
        if prime_graph[i][j] != replica_graph[i][j]:
            print(-1)
            exit(0)
print(ans)