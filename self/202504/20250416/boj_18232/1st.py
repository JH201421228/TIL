import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(s, e):
    q = deque([s])
    V[s] = 0

    while q:
        n = q.popleft()
        for x in G[n]:
            if V[x] == -1:
                if x == e:
                    return V[n]+1
                V[x] = V[n]+1
                q.append(x)


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
V = [-1] * (N+1)
G[1].append(2)
G[N].append(N-1)

for idx in range(2, N):
    G[idx].append(idx-1)
    G[idx].append(idx+1)

S, E = map(int, input().split())

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(bfs(S, E))