import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
for _ in range(M):
    i, j, dist = map(int, input().split())
    if graph[i-1][j-1] <= dist:
        print('Enjoy other party')
    else:
        print('Stay here')