import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(6_400)


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = []

    for _ in range(N):
        graph.append(list(map(str, input().rstrip())))

    t = 0
    c = 0
    for i in range(N):
        for j in range(0, M, 2):
            c += 1
            if graph[i][j] == '.':
                graph[i][j] = c
                t += 1

    G = [[] for _ in range(c+1)]

    d = 0
    for i in range(N):
        for j in range(1, M, 2):
            d += 1
            if graph[i][j] == '.':
                graph[i][j] = d
                t += 1

    C = [0] * (d+1)

    delta = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]

    for i in range(N):
        for j in range(0, M, 2):
            for di, dj in delta:
                if isinstance(graph[i][j], int) and i+di >= 0 and i+di < N and j+dj >= 0 and j+dj < M and isinstance(graph[i+di][j+dj], int):
                    G[graph[i][j]].append(graph[i+di][j+dj])

    a = 0
    for i in range(1, c+1):
        V = [0] * (d+1)
        if B(i):
            a += 1

    print(t-a)