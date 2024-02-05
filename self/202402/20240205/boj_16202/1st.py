import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline


N, M, K = map(int, input().split())
graph = deque([])
for i in range(M):
    temp = list(map(int, input().split()))
    temp.append(i+1)
    graph.append(temp)
# print(graph)


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

check = 0
ans = []
for _ in range(K):
    if not check:
        parent = [i for i in range(N+1)]
        way = 0
        cost = 0
        for a, b, c in graph:
            if not same_parent(a, b):
                union_parent(a, b)
                way += 1
                cost += c
        if way == N-1:
            ans.append(cost)
        else:
            ans.append(0)
            check = 1
        graph.popleft()
    else:
        ans.append(0)
print(*ans)