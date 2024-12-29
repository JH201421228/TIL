import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
sys.setrecursionlimit(10_000)
input = sys.stdin.readline


def find_KH(n, m):
    KH = [(0, 0), (0, 0)]
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 'K':
                KH[0] = (i, j)
            elif MAP[i][j] == 'H':
                KH[1] = (i, j)

    return KH

def set_edge(u, v):
    G[u].append(v)
    G[v].append(u)
    C[(u, v)] = 1
    C[(v, u)] = 0

def delta_search(n, m):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            for di, dj in delta:
                if i+di >= 0 and i+di < n and j+dj >= 0 and j+dj < m and MAP[i][j] != '#' and MAP[i+di][j+dj] != '#':
                    if (MAP[i][j] == 'K' and MAP[i+di][j+dj] == 'H') or (MAP[i][j] == 'H' and MAP[i+di][j+dj] == 'K'):
                        print(-1)
                        exit(0)
                    elif MAP[i][j] == 'K' or MAP[i][j] == 'H':
                        set_edge(i*m+j+1, (i+di)*m+(j+dj)+1)
                    else:
                        set_edge(n*m+i*m+j+1, (i+di)*m+(j+dj)+1)

def bfs(src, sink, n):
    L = [-1] * (2*n+1)
    L[src] = 0
    q = deque([src])

    while q:
        u = q.popleft()

        for v in G[u]:
            if L[v] == -1 and C[(u, v)] > 0:
                L[v] = L[u]+1
                q.append(v)

    if L[sink] == -1:
        return []
    else:
        return L

def dfs(u, sink, L):
    if u == sink:
        return 1

    for v in G[u]:
        if L[v] == L[u]+1 and C[(u, v)] > 0:
            k = dfs(v, sink, L)
            if k:
                C[(u, v)] -= 1
                C[(v, u)] += 1
                return 1

    return 0

def get_ans(src, sink, n):
    ans = 0

    while True:
        L = bfs(src, sink, n)

        if L:
            while True:
                flow = dfs(src, sink, L)
                if not flow:
                    break
                ans += flow
        else:
            return ans

N, M = map(int, input().split())

G = [[] for _ in range(2*N*M+1)]
C = defaultdict(int)

MAP = []
for _ in range(N):
    MAP.append(list(map(str, input().rstrip())))

KH = find_KH(N, M)

for i in range(N):
    for j in range(M):
        if MAP[i][j] == '.':
            set_edge(i*M+j+1, N*M+i*M+j+1)

delta_search(N, M)

print(get_ans(KH[0][0]*M+KH[0][1]+1, KH[1][0]*M+KH[1][1]+1, N*M))