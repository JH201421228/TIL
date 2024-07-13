import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10_000)


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
S, Ss, Sg = [], [[0]*M for _ in range(N)], [[0]*M for _ in range(N)]

for _ in range(N):
    S.append(list(map(str, input().rstrip())))

cnt_s, cnt_g = 0, 0
for i in range(N):
    for j in range(M):
        if S[i][j] == 'S':
            Ss[i][j] = cnt_s = cnt_s+1
        elif S[i][j] == 'G':
            Sg[i][j] = cnt_g = cnt_g+1

G = [[] for _ in range(cnt_s+1)]
C = [0] * (cnt_g+1)

delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
for i in range(N):
    for j in range(M):
        if S[i][j] == 'S':
            for di, dj in delta:
                ii, jj = i+di, j+dj
                if ii >= 0 and ii < N and jj >= 0 and jj < M:
                    if S[ii][jj] == 'G':
                        if (i+2*di >= 0 and i+2*di < N and j+2*dj >= 0 and j+2*dj < M and S[i+2*di][j+2*dj] == 'M') or (i-di >= 0 and i-di < N and j-dj >= 0 and j-dj < M and S[i-di][j-dj] == 'M'):
                            G[Ss[i][j]].append(Sg[ii][jj])

ans = 0
for i in range(1, cnt_s+1):
    V = [0]*(cnt_g+1)
    if B(i):
        ans += 1

print(ans)