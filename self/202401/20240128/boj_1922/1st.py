import sys
sys.stdin  =open('input.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = []

for _ in range(M):
    a, b, c = map(int, input().split())
    if a != b:
        graph.append((a, b, c))

graph.sort(key=lambda x: x[2])

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


ans = 0
for a, b, c in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        ans += c
print(ans)