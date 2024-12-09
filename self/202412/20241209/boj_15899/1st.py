import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(200_000)
input = sys.stdin.readline


MOD = 1_000_000_007

def dfs(n):
    global cnt
    A[n] = cnt = cnt+1
    T[cnt] = n
    for x in G[n]:
        if not A[x]:
            dfs(x)
    E[n] = cnt

def I(s, e, idx):
    if s == e:
        tree[idx] = [arr[T[s]]]
        return tree[idx]

    mid = (s+e) >> 1

    tree[idx] = merge(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1))
    return tree[idx]

def merge(X, Y):
    res = []
    i, j, x, y = 0, 0, len(X), len(Y)

    while i < x and j < y:
        if X[i] >= Y[j]:
            res.append(Y[j])
            j += 1
        else:
            res.append(X[i])
            i += 1
    res += X[i:]
    res += Y[j:]

    return res

def S(s, e, idx, l, r, c):
    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return count(tree[idx], c) % MOD

    mid = (s+e) >> 1
    return (S(s, mid, idx<<1, l, r, c) + S(mid+1, e, idx<<1|1, l, r, c)) % MOD

def count(X, c):
    s, e = 0, len(X)-1

    while s <= e:
        mid = (s+e) >> 1

        if X[mid] > c:
            e = mid-1
        else:
            s = mid+1

    return e+1


N, M, C = map(int, input().split())
arr = [0] + list(map(int, input().split()))

A = [0] * (N+1)
E = [0] * (N+1)
T = [0] * (N+1)
tree = [[] for _ in range(4*N+1)]
cnt = 0
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dfs(1)

I(1, N, 1)

ans = 0
for _ in range(M):
    v, c = map(int, input().split())
    ans += S(1, N, 1, A[v], E[v], c)
    ans %= MOD

print(ans)