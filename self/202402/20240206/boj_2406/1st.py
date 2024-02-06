import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = []
for _ in range(M):
    a, b = map(int, input().split())
    graph.append((a, b, 0))
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



matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i+1, N):
        graph.append((i+1, j+1, matrix[i][j]))
graph.sort(key=lambda x: x[2])
# print(graph)

ans = 0
check = 0
plus = 0
ans_list = []
for a, b, c in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        ans += c
        check += 1
        if c:
            plus += 1
            ans_list.append((a, b))

if ans:
    print(ans, plus)
    for inner in ans_list:
        print(*inner)
else:
    print(0, 0)