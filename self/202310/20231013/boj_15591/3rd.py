import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p1, p2, p = map(int, input().split())
    graph[p1].append((p2, p))
    graph[p2].append((p1, p))

for _ in range(Q):
    K, V = map(int, input().split())
    visited = [0] * (N+1)
    visited[K] = 1
    ans = 0
    q = deque([(V, float('inf'))])

    while q:
        now, now_point = q.popleft()
        for next, next_point in graph[now]:
            next_point = min(now_point, next_point)
            if next_point >= K and not visited[next]:
                ans += 1
                visited[next] = 1
                q.append((next, next_point))
    print(ans)