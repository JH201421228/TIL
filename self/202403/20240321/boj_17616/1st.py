import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


N, M, X = map(int, input().split())
front = 1
back = N
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph1[a].append(b)
    graph2[b].append(a)

visited = [0] * (N+1)
visited[X] = 1
q = deque([X])

while q:
    now = q.popleft()
    for next in graph1[now]:
        if not visited[next]:
            visited[next] = 1
            q.append(next)
            back -= 1

visited = [0] * (N+1)
visited[X] = 1
q = deque([X])

while q:
    now = q.popleft()
    for next in graph2[now]:
        if not visited[next]:
            visited[next] = 1
            q.append(next)
            front += 1

print(front, back)
