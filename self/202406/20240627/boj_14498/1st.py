import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(512)


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


N, M, K = map(int, input().split())
Gn, Gm = [], []

for _ in range(K):
    temp = list(map(int, input().split()))
    if temp[-1]:
        Gm.append((temp[0], temp[1]))
    else:
        Gn.append((temp[0], temp[1]))

Ln, Lm = len(Gn), len(Gm)
G = [[] for _ in range(Ln+1)]

for i in range(1, Ln+1):
    for j in range(1, Lm+1):
        if Gn[i-1][0] == Gm[j-1][0] or Gn[i-1][1] == Gm[j-1][1]:
            G[i].append(j)

ans = 0
C = [0] * (Lm+1)
for i in range(1, Ln+1):
    V = [0] * (Lm+1)
    if B(i):
        ans += 1

print(ans)