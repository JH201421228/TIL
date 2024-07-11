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
L = int(input())
lines = [[] for _ in range(N*M+1)]

for _ in range(L):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
G = [[] for _ in range(N*M+1)]

for i in range(N):
    for j in range(M):
        if not (i+j)%2:
            n = i*M+j+1
            for di, dj in delta:
                if i+di >= 0 and i+di < N and j+dj >= 0 and j+dj < M:
                    nn = (i+di)*M+(j+dj)+1
                    if nn not in lines[n]:
                        G[n].append(nn)

C = [0] * (N*M+1)

for i in range(N):
    for j in range(M):
        if not (i+j)%2:
            V = [0] * (N*M+1)
            B(i*M+j+1)

for i in range(N):
    for j in range(M):
        if (i+j)%2:
            print((i*M+j+1), C[i*M+j+1])