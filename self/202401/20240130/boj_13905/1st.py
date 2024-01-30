import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
S, E = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(tuple(map(int, input().split())))
graph.sort(reverse=True, key=lambda x: x[2])

parent = [i for i in range(N+1)]


def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = parent[x]
    y = parent[y]
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def same_parent(x, y):
    return find_parent(x) == find_parent(y)

way = [[] for _ in range(N+1)]
for a, b, c in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        way[a].append((b, c))
        way[b].append((a, c))
# print(parent)
# print(way)


visited = [0 for _ in range(N+1)]
visited[S] = 1
q = deque([(S, float('inf'))])
ans = 0

while q:
    now, now_weight = q.popleft()
    if now == E:
       ans = now_weight
       break
    for next, weight in way[now]:
        if not visited[next]:
            now_weight = min(now_weight, weight)
            q.append((next, now_weight))
            visited[next] = 1

print(ans)
