import sys
sys.setrecursionlimit(100_000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def scc(n):
    global O, cnt

    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]:
            p = min(p, scc(x))
        elif not F[x]:
            p = min(p, V[x])

    if p == V[n]:
        while S:
            o = S.pop()
            F[o] = p
            if o == n:
                break

    return p


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

O, cnt = 0, 0

V = [0] * (N+1)
F = [0] * (N+1)
S = []

for _ in range(M):
    u, v = map(int, input().split())
    G[u+1].append(v+1)

for n in range(1, N+1):
    if not V[n]:
        scc(n)

checker = {i: [] for i in set(F[1:])}

for s in range(1, N+1):
    for e in G[s]:
        if F[e] != F[s]:
            checker[F[e]].append(F[s])

ans = 0
for k, v in checker.items():
    if not v:
        ans += 1

print(ans)