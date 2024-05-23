import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


N, M = map(int, input().split())
start_point = [True] * (N+1)
order_dict = {}
order_list = [[] for _ in range(N+1)]
ans = []

for _ in range(M):
    s, e = map(int, input().split())
    start_point[e] = False
    heapq.heappush(order_list[s], e)
    order_dict[e] = order_dict.get(e, 0) + 1

q = []
for idx in range(1, N+1):
    if start_point[idx]:
        heapq.heappush(q, idx)

while q:
    now = heapq.heappop(q)
    while order_list[now]:
        next = heapq.heappop(order_list[now])
        order_dict[next] = order_dict.get(next) - 1
        if not order_dict[next]:
            heapq.heappush(q, next)
    ans.append(now)

print(*ans)