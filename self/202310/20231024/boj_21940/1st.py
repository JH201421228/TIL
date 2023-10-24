import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start][end] = time

K = int(input())
K_list = list(map(int, input().split()))

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i==j:
                graph[i][i] = 0
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans_list = []
for i in range(1, N+1):
    temp = []
    for j in K_list:
        temp.append(graph[i][j] + graph[j][i])
    ans_list.append(max(temp))

min_val = min(ans_list)
for idx in range(N):
    if ans_list[idx] == min_val:
        print(idx+1, end=' ')