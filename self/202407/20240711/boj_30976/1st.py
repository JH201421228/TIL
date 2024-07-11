import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(500)


def B(n):
    for x in G[n]:
        if V[x]:
            continue

        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


N, M = map(int, input().split())

P = []

for _ in range(4):
    P.append(tuple(map(int, input().split())))

G = [[] for _ in range(N+1)]
C = [0] * (M+1)

for i in range(1, N+1):
    for j in range(1, M+1):
        i_, j_, Pi, Pj = P[0][i-1], P[1][j-1], P[2][i-1], P[3][j-1]

        if i_ > Pj and j_ < Pi:
            G[i].append(j)

ans = 0

for i in range(1, N+1):
    V = [0] * (M+1)
    if B(i):
        ans += 1

print(ans)