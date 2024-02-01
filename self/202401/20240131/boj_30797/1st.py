import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, Q = map(int, input().split())
graph = []
for _ in range(Q):
    graph.append(tuple(map(int, input().split())))

graph.sort(key=lambda x: (x[2], x[3]))

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

time = 0
cost = 0
checker = 0
for a, b, c, d in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        checker += 1
        cost += c
        time = max(time, d)
if checker == N-1:
    print(time, cost)
else:
    print(-1)
