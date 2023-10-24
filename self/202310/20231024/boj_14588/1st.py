import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
line_info = []

for _ in range(N):
    start, end = map(int, input().split())
    line_info.append((start, end, end - start))

for i in range(N):
    for j in range(i+1, N):
        s1, e1, len1 = line_info[i]
        s2, e2, len2 = line_info[j]
        if max(e1, e2) - min(s1, s2) <= len1 + len2:
            graph[i+1][j+1] = graph[j+1][i+1] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            graph[i][j] = graph[j][i] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(int(input())):
    start, end = map(int, input().split())
    dist = graph[start][end]
    if dist != float('inf'):
        print(dist)
    else:
        print(-1)