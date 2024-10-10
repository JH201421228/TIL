import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_scc(n):
    global O, GN

    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if V[x] == -1:
            p = min(p, find_scc(x))
        elif not F[x]:
            p = min(p, V[x])

    if p == V[n]:
        temp = []

        while S:
            out = S.pop()
            temp.append(out)
            F[out] = 1

            if out == n:
                GR.append(temp)
                break

    return p


N = int(input())
C = list(map(int, input().split()))
G = [[] for _ in range(N)]

V = [-1] * N
F = [0] * N
S = []
O = 0
GR = []

for i in range(N):
    temp = list(map(int, input().rstrip()))

    for j in range(N):
        if temp[j]:
            G[i].append(j)

for i in range(N):
    if V[i] == -1:
        find_scc(i)

ans = 0
for inner in GR:
    v = float('inf')

    for u in inner:
        v = min(v, C[u])

    ans += v

print(ans)