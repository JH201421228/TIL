import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = graph[end][start] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][j] = 0
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans_list = []
for inner in graph[1:]:
    ans_list.append(sum(inner[1:]) - max(inner[1:]))

ans = ans_list.index(min(ans_list)) + 1
another = graph[ans].index(max(graph[ans][1:]))
sum_val = (sum(graph[ans][1:]) - graph[ans][another]) * 2

if ans > another:
    print(another)
    print(ans)
else:
    print(ans)
    print(another)
print(sum_val)