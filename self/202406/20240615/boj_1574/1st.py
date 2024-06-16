import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not D[x] or B(D[x]):
            D[x] = n
            return True

    return False


R, C, N = map(int, input().split())
board = [[1] * C for _ in range(R)]

for _ in range(N):
    a, b = map(int, input().split())
    board[a-1][b-1] = 0

G = [[] for _ in range(R+1)]
for i in range(R):
    for j in range(C):
        if board[i][j]:
            G[i+1].append(j+1)

D = [0] * (C+1)
ans = 0
for i in range(1, R+1):
    V = [0] * (C+1)
    if B(i):
        ans += 1

print(ans)