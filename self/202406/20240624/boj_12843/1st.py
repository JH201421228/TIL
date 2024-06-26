import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(2_000)


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not D[x] or B(D[x]):
            D[x] = n
            return True

    return False


N, M = map(int, input().split())
C = [0] * (N+1)
for _ in range(N):
    a, b = map(str, input().rstrip().split())
    if b == 'c':
        C[int(a)] = 1

G = [[] for _ in range(N+1)]
D = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    if C[a]:
        G[a].append(b)
    else:
        G[b].append(a)

ans = 0
for i in range(1, N+1):
    if C[i]:
        V = [0] * (N+1)
        if B(i):
            ans += 1

print(N-ans)