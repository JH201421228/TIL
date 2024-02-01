import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = []
for _ in range(N - M + 1):
    graph.append(tuple(map(int, input().split())))
parent = [i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    parent[max(a, b)] = min(a, b)

way = [(0, 0, float('inf'))]
for i in range(N-M+1):
    for j in range(i+1, N-M+1):
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


ans = 0
for a, b, c in way:
    if not same_parent(a, b):
        union_parent(a, b)
        ans += c


print(f'{ans:.2f}')