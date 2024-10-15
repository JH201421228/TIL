import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(200_000)
input = sys.stdin.readline


def scc(n):
    global O, C

    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]:
            p = min(p, scc(x))
        elif not F[x]:
            p = min(p, V[x])

    if p == V[n]:
        C += 1
        while S:
            out = S.pop()
            F[out] = C

            if out == n:
                break

    return p


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)

V = [0] * (N+1)
F = [0] * (N+1)
O = 0
C = 0
S = []

for i in range(1, N+1):
    if not V[i]:
        scc(i)

if C == 1:
    print("Yes")
else:
    print("No")