import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


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
G = [[] for _ in range(N+1)]
C = [0] * (M+1)

for _ in range(K):
    a, b = map(int, input().split())
    G[a].append(b)

ans = N + M
for i in range(1, N+1):
    V = [0] * (M+1)
    if B(i):
        ans -= 1

print(ans)