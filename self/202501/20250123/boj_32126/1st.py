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


N, K = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]

G = [[] for _ in range(K+1)]

for t in range(K):
    for d in range(N):
        if M[d][t]:
            G[K-t].append(d+1)

C = [0] * (N+1)
ans = 0
camera = 0

for n in range(1, K+1):
    V = [0] * (N+1)

    if B(n):
        if (ans-camera)+2 > K+1-n:
            break
        ans += 1

    else:
        if camera < ans:
            camera += 1

print(ans)