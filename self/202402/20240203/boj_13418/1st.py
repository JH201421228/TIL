import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = []
for _ in range(M+1):
    graph.append(tuple(map(int, input().split())))


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


parent = [i for i in range(N+1)]
graph.sort(key=lambda x: x[2])

ans1 = 0
for a, b, c in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        if not c:
            ans1 += 1


parent = [i for i in range(N+1)]
graph.sort(key=lambda x: -x[2])

ans2 = 0
for a, b, c in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        if not c:
            ans2 += 1

print(ans1**2 - ans2**2)