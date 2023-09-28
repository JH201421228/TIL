from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

INF = float('inf')


def dijkstra(start, end):
    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    dp[start][0] = 0
    queue = [(0, 0, start)]

    while queue:
        curr_dist, curr_cnt, curr_node = heapq.heappop(queue)

        if curr_dist > dp[curr_node][curr_cnt]:
            continue

        for next_node, weight in adj[curr_node].items():
            distance = curr_dist + weight
            if distance < dp[next_node][curr_cnt + 1]:
                for i in range(curr_cnt + 1, N + 1):
                    if dp[next_node][i] > distance:
                        dp[next_node][i] = distance
                    else:
                        break
                heapq.heappush(queue, (distance, curr_cnt + 1, next_node))

    return dp


N, M, K = map(int, input().split())

S, D = map(int, input().split())

adj = defaultdict(dict)

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = c
    adj[b][a] = c

result = dijkstra(S, D)
print(min(result[D]))

pair = []
for i in range(1, len(result)):
    if result[D][i] != INF and result[D][i] != result[D][i - 1]:
        pair.append([i, result[D][i]])

for _ in range(K):
    tax = int(input())
    for i in range(len(pair)):
        pair[i][1] += pair[i][0] * tax

    print(min(pair, key=lambda x: x[1])[1])