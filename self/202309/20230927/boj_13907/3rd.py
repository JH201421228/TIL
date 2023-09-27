import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M, K = map(int, input().split())
S, D = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    if end > start:
        start, end = end, start
    graph[start].append((end, weight))
    # graph[end].append((start, weight))
graph[S], graph[1] = graph[1], graph[S]
taxs = [0]
tax = 0
for _ in range(K):
    tax += int(input())
    taxs.append(tax)

ans_list = [[float('inf')] * (30_001) for _ in range(N+1)]

ans_list[1][0] = 0
for roads in range(30_001):
    for now in range(1, N+1):
        if ans_list[now][roads] != float('inf'):
            for next, weight in graph[now]:
                if roads + 1 < 30_001 and ans_list[next][roads+1] > ans_list[now][roads] + weight:
                    ans_list[next][roads + 1] = ans_list[now][roads] + weight

ans = ans_list[-1]
ans_matrix = [[] for _ in range(K+1)]
for idx in range(30_001):
    if ans[idx] != float('inf'):
        for idx_k in range(K+1):
            ans_matrix[idx_k].append(ans[idx] + idx * taxs[idx_k])
# print(ans_matrix)
for inner in ans_matrix:
    if len(inner) > 1:
        print(min(inner))
    else:
        print(inner)