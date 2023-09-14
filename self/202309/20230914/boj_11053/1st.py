import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = list(map(int, input().split()))
graph = [[0] * N for _ in range(N)]
graph[0][0] = num_list[0]
for i in range(1, N):
    for j in range(i+1):
        if graph[i-1][j] < num_list[i]:
            graph[i][j] = num_list[i]
        else:
            graph[i][j] = graph[i-1][j]
for inner in graph:
    print(inner)
