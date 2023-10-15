import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    q = deque([1])
    visited = [0] * (N+1)
    visited[1] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
    return visited


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-2):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
visited = bfs()
for idx in range(1, N+1):
    if not visited[idx]:
        print(f'1 {idx}')
        break