import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def isOdd(n):
    if n % 2:
        return True

    return False


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
G = [[] for _ in range(N//2 + 2)]
C = [0] * (N//2 + 2)

for _ in range(M):
    a, b = map(int, input().split())

    if isOdd(a) != isOdd(b):
        if isOdd(a):
            G[a//2 + 1].append(b//2)
        else:
            G[b // 2 + 1].append(a // 2)

ans = 0
for i in range(1, N//2 + 2):
    V = [0] * (N//2 + 2)
    if B(i):
        ans += 2

if ans < N:
    ans += 1

print(ans)