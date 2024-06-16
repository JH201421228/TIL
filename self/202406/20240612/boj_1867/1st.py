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


N, K = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    G[a].append(b)

C = [0] * (N+1)

ans = 0
for i in range(1, N+1):
    V = [0] * (N+1)
    if B(i):
        ans += 1

print(ans)