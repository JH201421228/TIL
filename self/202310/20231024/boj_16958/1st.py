import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, T  = map(int, input().split())
graph = [[0] * N for _ in range(N)]
city_info = []

for _ in range(N):
    city_info.append(tuple(map(int, input().split())))

for i in range(N):
    for j in range(i+1, N):
        s1, x1, y1 = city_info[i]
        s2, x2, y2 = city_info[j]
        dist = abs(x1-x2) + abs(y1-y2)
        if s1*s2:
            graph[i][j] = graph[j][i] = min(dist, T)
        else:
            graph[i][j] = graph[j][i] = dist

for k in range(N):
    for i in range(N):
        for j in range(i+1, N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[j][i] = graph[i][k] + graph[k][j]

for _ in range(int(input())):
    start, end = map(int, input().split())
    print(graph[start-1][end-1])