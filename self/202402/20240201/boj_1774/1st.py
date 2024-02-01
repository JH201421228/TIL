import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(tuple(map(int, input().split())))
parent = [i for i in range(N+1)]
already = []

for _ in range(M):
    a, b = map(int, input().split())
    already.append((min(a, b), max(a, b)))
already.sort(key=lambda x: (-x[0]))

# print(already)
way = []
for i in range(N):
    for j in range(i+1, N):
        if (i+1, j+1) in already:
            way.append((i+1, j+1, float('inf')))
        way.append((i+1, j+1, ((graph[i][0]-graph[j][0])**2+(graph[i][1]-graph[j][1])**2)**0.5))
way.sort(key=lambda x: x[2])
# print(way)

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


for a, b in already:
    if not same_parent(a, b):
        union_parent(a, b)

ans = 0
for a, b, c in way:
    if not same_parent(a, b):
        union_parent(a, b)
        ans += c


print(format(ans, ".2f"))