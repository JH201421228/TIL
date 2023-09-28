import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def variable_tax():
    pq = [(0, 0, S)]
    ans_list = [[float('inf')] * (N+1) for _ in range(N + 1)]
    ans_list[S][0] = 0

    while pq:
        cost, dist, now = heapq.heappop(pq)
        if ans_list[now][dist] < cost:
            continue

        for next, weigth in graph[now]:
            new_cost = cost + weigth
            if new_cost < ans_list[next][dist + 1]:
                for i in range(dist+1, N+1):
                    if ans_list[next][i] > new_cost:
                        ans_list[next][i] = new_cost
                    else:
                        break
                heapq.heappush(pq, (cost + weigth, dist + 1, next))
    return ans_list[D]


N, M, K = map(int, input().split())
S, D = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))
graph[S], graph[1] = graph[1], graph[S]
taxs = [0]
tax = 0
for _ in range(K):
    tax += int(input())
    taxs.append(tax)

# ans_list = [[float('inf')] * (30_001) for _ in range(N+1)]
#
# ans_list[1][0] = 0

ans = variable_tax()
# print(ans)
ans_matrix = [[] for _ in range(K+1)]
for idx in range(1, N+1):
    if ans[idx] != float('inf') and ans[idx] != ans[idx - 1]:
        for idx_k in range(K+1):
            ans_matrix[idx_k].append(ans[idx] + idx * taxs[idx_k])
# print(ans_matrix)
for inner in ans_matrix:
    if len(inner) > 1:
        print(min(inner))
    else:
        print(*inner)