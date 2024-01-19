import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(n+1):
    for i in range(n+1):
        for j in range(i+1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            graph[j][i] = graph[i][j]

if graph[p1][p2] != float('inf'):
    print(graph[p1][p2])
else:
    print(-1)