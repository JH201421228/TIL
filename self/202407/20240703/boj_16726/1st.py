import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(2_500)


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
R = []
for _ in range(N):
    R.append(list(map(str, input().rstrip())))

cnt = 1
x = 1
for i in range(N):
    for j in range(M):
        if R[i][j] == '.':
            R[i][j] = cnt
        else:
            x += 1

        cnt += 1

G = [[] for _ in range(cnt + 1)]
C = [0] * (cnt + 1)
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N):
    for j in range(M):
        if not (i+j)%2 and R[i][j] != 'X':
            for di, dj in delta:
                if i+di >= 0 and i+di < N and j+dj >= 0 and j+dj < M and R[i+di][j+dj] != 'X':
                    G[R[i][j]].append(R[i+di][j+dj])

c = cnt

for i in range(1, cnt + 1):
    V = [0] * (cnt + 1)
    if B(i):
        c -= 1

print(c - x)