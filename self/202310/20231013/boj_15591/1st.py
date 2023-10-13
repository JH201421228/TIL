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
        for next in range(1, N+1):
            if not visited[next] and graph[now][next]:
                visited[next] = 1
                new_score = min(score, graph[now][next])
                q.append((next, new_score))
                if new_score >= K:
                    cnt += 1
    return cnt


N, Q = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    p1, p2, p = map(int, input().split())
    graph[p1][p2] = graph[p2][p1] = p
for _ in range(Q):
    K, V = map(int, input().split())
    print(bfs(V))

