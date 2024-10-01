import sys
import heapq
sys.stdin = open('input.txt')
sys.setrecursionlimit(100_000)
input = sys.stdin.readline


def find(x):
    if P[x] == x:
        return x

    P[x] = find(P[x])

    return P[x]


def union(x, y):
    x, y = find(x), find(y)

    if x > y:
        P[x] = y
    else:
        P[y] = x


N = int(input())

X, Y, Z = [], [], []

for i in range(N):
    a, b, c = map(int, input().split())

    X.append((a, i))
    Y.append((b, i))
    Z.append((c, i))

G = []

X.sort()
Y.sort()
Z.sort()

for i in range(N-1):
    G.append((X[i+1][0] - X[i][0], X[i][1], X[i+1][1]))
    G.append((Y[i+1][0] - Y[i][0], Y[i][1], Y[i+1][1]))
    G.append((Z[i+1][0] - Z[i][0], Z[i][1], Z[i+1][1]))

G.sort()

P = [i for i in range(N)]

cnt = 0
ans = 0
idx = 0

while cnt < N-1:
    c, a, b = G[idx]
    idx += 1

    if find(a) != find(b):
        ans += c
        cnt += 1

        union(a, b)

print(ans)