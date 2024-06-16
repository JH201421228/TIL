import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(5_000)


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
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

Ve, Ho = [[0] * M for _ in range(N)], [[0] * M for _ in range(N)]
cnt_v, cnt_h = 1, 1

for j in range(M):
    for i in range(N):
        if not board[i][j]:
            Ve[i][j] = cnt_v
        elif board[i][j] == 2:
            cnt_v += 1
    cnt_v += 1

for i in range(N):
    for j in range(M):
        if not board[i][j]:
            Ho[i][j] = cnt_h
        elif board[i][j] == 2:
            cnt_h += 1
    cnt_h += 1

G = [[] for _ in range(cnt_v+1)]
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            G[Ve[i][j]].append(Ho[i][j])

C = [0] * (cnt_h+1)
ans = 0
for i in range(1, cnt_v+1):
    V = [0] * (cnt_h+1)
    if B(i):
        ans += 1

print(ans)