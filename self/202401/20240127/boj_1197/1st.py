import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
for _ in range(E):
    graph.append(tuple(map(int, input().split())))
graph.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def is_same_parent(x, y):
    return find_parent(x) == find_parent(y)

ans = 0
for a, b, c in graph:
    if not is_same_parent(a, b):
        union_parent(a, b)
        ans += c

print(ans)