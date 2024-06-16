import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1_000)


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
G = [[]]
for _ in range(N):
    G.append(list(map(int, input().split()))[1:])

C = [0] * (M+1)
A = [1] * (N+1)

ans = 0
for i in range(1, N+1):
    V = [0] * (M+1)
    if B(i):
        ans += 1
    else:
        A[i] = 0

k = 0
while True:
    c = 0
    for i in range(1, N+1):
        if A[i]:
            V[0] * (M+1)
            if B(i):
                ans += 1
                k += 1
                c += 1
            else:
                A[i] = 0

        if k == K:
            break
    if k == K or not c:
        break

print(ans)