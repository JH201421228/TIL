import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(500_000)


def find_scc(now):
    global cnt, val
    parent = V[now] = val = val + 1
    S.append(now)

    for nxt in G[now]:
        if not V[nxt]:
            parent = min(parent, find_scc(nxt))
        elif not F[nxt]:
            parent = min(parent, V[nxt])

    if parent == V[now]:
        cnt += 1
        while S:
            out = S.pop()
            F[out] = 1
            H[out] = cnt
            if out == now:
                break

    return parent


N, M, C, K = map(int, input().split())
I = list(map(int, input().split()))
U = [0] * (N+1)
G = [[] for _ in range(2*N+1)]
V = [0] * (2*N+1)
F = [0] * (2*N+1)
H = [0] * (2*N+1)
S = []
cnt = val = 0

for _ in range(C):
    a, b = map(int, input().split())
    G[-a].append(b)
    G[-b].append(a)
    U[a] = U[b] = 1

for _ in range(K):
    a, b = map(int, input().split())
    a, b = -a, -b
    G[-a].append(b)
    G[-b].append(a)

for a in I:
    if not U[a]:
        G[-a].append(a)

for idx in range(-N, N+1):
    if idx and not V[idx]:
        find_scc(idx)

for idx in range(1, N+1):
    if H[idx] == H[-idx]:
        print('NO')
        exit(0)

print('YES')