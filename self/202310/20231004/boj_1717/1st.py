import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(60000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
for _ in range(m):
    k, a, b = map(int, input().split())
    if k:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
# print(parent)