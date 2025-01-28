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
            C[n] = x
            return True

    return False


N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

G = [[] for _ in range(N**2+1)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

temp = [[] for _ in range(N**2+1)]

for i in range(N**2):
    x, y = i // N, i % N
    if x % 2 + y % 2 != 1:
        for dx, dy in delta:
            xx, yy = x+dx, y+dy
            if xx >= 0 and xx < N and yy >= 0 and yy < N:
                temp[max(M[x][y], M[xx][yy])].append((x*N+y+1, xx*N+yy+1))

U = [0] * (N**2+1)
C = [0] * (N**2+1)
ans = []
for i in range(1, N**2+1):
    if temp[i]:
        for u, v in temp[i]:
            G[u].append(v)
            G[v].append(u)

        for u, v in temp[i]:
            if not U[u] and not U[v]:
                U[u] = 1
                U[v] = 1
                C[u] = v
                C[v] = u
                ans.append(i)
            elif not U[u]:
                U[u] = 1
                V = [0] * (N**2+1)
                if B(u):
                    ans.append(i)
            elif not U[v]:
                U[v] = 1
                V = [0] * (N**2+1)
                if B(v):
                    ans.append(i)

for n in ans:
    print(n)