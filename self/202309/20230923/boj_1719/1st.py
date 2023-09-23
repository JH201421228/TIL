import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


n, m = map(int, input().split())
ans_graph = [[float('inf') for _ in range(n)] for _ in range(n)]
# print(ans_graph)
# for i in range(n):
#     ans_graph[i][i] = 0
real_ans_graph = [['-'] * n for _ in range(n)]
for _ in range(m):
    p1, p2, point = map(int, input().split())
    ans_graph[p1-1][p2-1] = point
    ans_graph[p2-1][p1-1] = point
    real_ans_graph[p1-1][p2-1] = p2
    real_ans_graph[p2-1][p1-1] = p1
for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                ans_graph[j][k] = '-'
            elif j != i and i != k:
                new_dist = ans_graph[j][i] + ans_graph[i][k]
                if new_dist < ans_graph[j][k]:
                    ans_graph[j][k] = new_dist
                    real_ans_graph[j][k] = real_ans_graph[j][i]
                # ans_graph[j][k] = min(ans_graph[j][k], ans_graph[j][i] + ans_graph[i][k])
# for inner in ans_graph:
#     print(*inner)
for inner in real_ans_graph:
    print(*inner)
