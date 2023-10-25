import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or i == k or j == k:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][k])
print(graph)
