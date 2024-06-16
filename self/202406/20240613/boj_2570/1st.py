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


N = int(input())
board = [[1] * (N+1) for _ in range(N+1)]
for _ in range(int(input())):
    i, j = map(int, input().split())
    board[i][j] = 0

G = [[] for _ in range(2*N)]
for i in range(1, 2*N):
    for j in range(1, 2*N):
        k, l = -N + i, 1 + j
        if not (k+l)%2 and not (l-k)%2:
            i_, j_ = (k+l)//2, (l-k)//2
            if i_ >= 1 and i_ <= N and j_ >= 1 and j_ <= N and board[i_][j_]:
                G[i].append(j)

C = [0] * (2*N)
ans = 0
for i in range(1, 2*N):
    V = [0] * (2*N)
    if B(i):
        ans += 1

print(ans)
print(G)
print(C)