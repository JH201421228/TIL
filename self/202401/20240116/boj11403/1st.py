import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# print(graph)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] or (graph[i][k] and graph[k][j]):
                graph[i][j] = 1
for inner in graph:
    print(*inner)