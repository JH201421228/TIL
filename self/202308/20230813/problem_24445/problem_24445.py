import sys
from collections import deque
# sys.stdin = open('input.txt')


def BFS(V, start):
    que = deque([start])
    cnt = 1
    trace = [0] * (V+1)
    trace[start] = cnt

    while que:
        now = que.popleft()
        graph[now].sort(reverse=True)
        for next in graph[now]:
            if not trace[next]:
                cnt += 1
                trace[next] = cnt
                que.append(next)
    return trace

V, E, start = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
ans = BFS(V, start)

for i in range(1, len(ans)):
    print(ans[i])