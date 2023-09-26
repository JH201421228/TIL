import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def KCM():
    pq = [(0, 0, 1)]
    # time_line = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
    # time_line[1][0] = 0
    # visited = [0] * (N+1)
    # visited[1] = 1
    while pq:
        time, dist, now = heapq.heappop(pq)
        # if time_line[now][time] < dist:
        #     continue
        if now == N and dist <= M:
            return time
        for next, weight, next_time in graph[now]:
            if dist + weight < M+1:
                heapq.heappush(pq, (next_time + time, dist + weight, next))
    return 'Poor KCM'


T = int(input())
N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(K):
    start, end, point, time = map(int, input().split())
    graph[start].append((end, point, time))
# ans = min(KCM())
# if ans == float('inf'):
#     print('Poor KCM')
# else:
#     print(ans)
print(KCM())