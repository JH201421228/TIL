import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(start):
    q = deque([(start, float('inf'))])
    visited = [0] * (N+1)
    visited[start] = 1
    cnt = 0
    while q:
        now, score = q.popleft()
        for next, n_score in graph[now]:
            min_val = min(score, n_score)
            if not visited[next] and min_val >= K:
                visited[next] = 1
                q.append((next, min_val))
                cnt += 1
    return cnt


N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p1, p2, p = map(int, input().split())
    graph[p1].append((p2, p))
    graph[p2].append((p1, p))
for _ in range(Q):
    K, V = map(int, input().split())
    print(bfs(V))

