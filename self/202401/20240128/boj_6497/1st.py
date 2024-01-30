import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


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


while True:
    M, N = map(int, input().split())
    if not M and not N:
        break
    graph = []

    for _ in range(N):
        graph.append(tuple(map(int, input().split())))

    graph.sort(key=lambda x: x[2])

    parent = [i for i in range(M)]

    ans = 0
    total = 0
    for a, b, c in graph:
        total += c
        if not same_parent(a, b):
            union_parent(a, b)
            ans += c
    print(total - ans)