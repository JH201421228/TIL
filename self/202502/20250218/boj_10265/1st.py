import sys
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
        cnt += 1
        while S:


    return p


N, K = map(int, input().split())

G = [[] for _ in range(N+1)]

temp = list(map(int, input().split()))

for idx in range(N):
    G[idx+1].append(temp[idx])

S = []
F = [0] * (N+1)
V = [0] * (N+1)
for n in range(1, N+1):
    if not V[n]:
        scc(n)