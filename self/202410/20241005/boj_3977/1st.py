import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100_000)
input = sys.stdin.readline


def find_scc(n):
    global O, GN

    P = V[n] = O = O + 1
    S.append(n)

    for x in G[n]:
        if V[x] == -1:
            P = min(P, find_scc(x))
        elif F[x] == -1:
            P = min(P, V[x])

    if P == V[n]:
        while S:
            o = S.pop()
            F[o] = GN
            if o == n:
                break
        GN += 1

    return P

for _ in range(int(input())):
    N, M = map(int, input().split())
    O = 0
    V = [-1] * N
    F = [-1] * N
    G = [[] for _ in range(N)]
    S = []
    GN = 0

    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)

    input()

    for n in range(N):
        if V[n] == -1:
            find_scc(n)

    GC = [0] * GN

    for i in range(N):
        for j in G[i]:
            if F[i] != F[j]:
                GC[F[j]] += 1

    temp = []

    for i in range(GN):
        if not GC[i]:
            temp.append(i)

    if len(temp) > 1:
        print("Confused")
    else:
        for i in range(N):
            if F[i] == temp[0]:
                print(i)

    print()