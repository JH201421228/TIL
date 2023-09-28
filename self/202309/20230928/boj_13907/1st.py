import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def holiday():
    pq = [(0, 0, S)]
    ans_list = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    ans_list[S][0] = 0

    while pq:
        cost, cnt, now = heapq.heappop(pq)
        if ans_list[now][cnt] < cost:
            continue
        for next, weight in graph[now]:
            next_cost = cost + weight
            if ans_list[next][cnt+1] > next_cost:
                for idx in range(cnt+1, N+1):
                    if ans_list[next][idx] > next_cost:
                        ans_list[next][idx] = next_cost
                    else:
                        break
                heapq.heappush(pq, (next_cost, cnt+1, next))
    return ans_list[D]


N, M, K = map(int, input().split())
S, D = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))

taxs = [0]
for _ in range(K):
    taxs.append(taxs[-1] + int(input()))

ans = holiday()
# print(ans)
real_ans = []
for tax in taxs:
    min_cost = float('inf')
    for cnt, cost in enumerate(ans):
        min_cost = min(min_cost, cost + cnt * tax)
    real_ans.append(min_cost)

for idx in range(K+1):
    print(real_ans[idx])