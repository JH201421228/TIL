import sys
import heapq
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
G = [list(map(int, input().split())) for _ in range(N)]
E = []

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N):
    for j in range(N):
        if not (i+j) % 2:
            for di, dj in delta:
                if 0 <= i+di < N and 0 <= j+dj < N:
                    heapq.heappush(E, [max(G[i][j], G[i+di][j+dj]), (i*N+j)//2+1, ((i+di)*N+j+dj)//2+1])


G = [[] for _ in range(N**2//2+1)]
ans = []
C = [0] * (N**2//2+1)
check = 0

while E:
    v, a, b = heapq.heappop(E)
    G[a].append(b)

    if not ans or ans[-1] < v:
        copy = [*C]
        C[a] = 0
        V = [0] * (N**2//2+1)
        if B(a):
            cnt = 0
            for i in C[1:]:
                if i:
                    cnt += 1
            if cnt > check:
                ans.append(v)
                check += 1
                G[a] = []
            else:
                C = [*copy]

for a in ans:
    print(a)