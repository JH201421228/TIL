import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10_000)


def D(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or D(C[x]):
            C[x] = n
            return True

    return False


N = int(input())
board = [[1] * (N+1) for _ in range(N+1)]
for _ in range(int(input())):
    i, j = map(int, input().split())
    board[i][j] = 0

A, B = [[0] * (N+1) for _ in range(N+1)], [[0] * (N+1) for _ in range(N+1)]

n = 1
for s in range(2, 2*N+1):
    for i in range(1, N+1):
        j = s - i
        if i >= 1 and i <= N and j >= 1 and j <= N:
            if board[i][j]:
                A[i][j] = n
            else:
                n += 1
    n += 1

n = 1
for s in range(-N+1, N):
    for i in range(1, N+1):
        j = s + i
        if i >= 1 and i <= N and j >= 1 and j <= N:
            if board[i][j]:
                B[i][j] = n
            else:
                n += 1
    n += 1

G = [[] for _ in range(n+1)]
C = [0] * (n+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        if board[i][j]:
            G[A[i][j]].append(B[i][j])

ans = 0
for i in range(1, n+1):
    V = [0] * (n+1)
    if D(i):
        ans += 1

print(ans)