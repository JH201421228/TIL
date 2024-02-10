import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M, K = map(int, input().split())
stone_info = list(map(int, input().split()))
# M == 0이면 이을 필요 없음

input_info = []
for _ in range(M):
    input_info.append(tuple(map(int, input().split())))

if (N, 1) in input_info or (1, N) in input_info:
    graph = [(N, 1, float('inf'))]
else:
    graph = [(N, 1, 0)]

for i in range(1, N):
    if (i, i+1) in input_info or (i+1, i) in input_info:
        graph.append((i, i+1, float('inf')))
    else:
        graph.append((i, i+1, 0))

for i in range(N):
    graph.append((0, i+1, stone_info[i]))
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


cost = 0
way = 0
for a, b, c in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        cost += c

if M == 0 or cost <= K:
    print('YES')
else:
    print('NO')