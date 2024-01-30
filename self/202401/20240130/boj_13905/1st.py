import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

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
def dfs(now, val):
    if now == E:
        print(val)
        exit(0)
    for next, cost in way[now]:
        if not visited[next]:
            visited[next] = 1
            dfs(next, min(cost, val))
            visited[next] = 0


dfs(S, float('inf'))

