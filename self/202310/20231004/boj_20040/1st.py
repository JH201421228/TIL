import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b, idx):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    elif b > a:
        parent[b] = a
    else:
        global ans
        if not ans:
            ans = idx


n, m = map(int, input().split())
parent = [0] * n
ans = 0
for idx in range(n):
    parent[idx] = idx
for idx in range(m):
    a, b = map(int, input().split())
    union(a, b, idx + 1)
print(ans)