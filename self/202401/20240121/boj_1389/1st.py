import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = 1


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            graph[i][j] = graph[j][i] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# for inner in graph:
#     print(inner)

ans_list = [float('inf')]
for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        if graph[i][j] == float('inf'):
            continue
        temp += graph[i][j]
    ans_list.append(temp)

# print(ans_list)
print(ans_list.index(min(ans_list)))