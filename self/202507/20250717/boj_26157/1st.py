import sys
from collections import deque
sys.setrecursionlimit(200_000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def scc(n):
    global S, V, F, G, O, Z

    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]: p = min(p, scc(x))
        elif not F[x]: p = min(p, V[x])

    if p == V[n]:
        Z += 1

        while S:
            o = S.pop()
            F[o] = Z

            if n == o: break

    return p


def generate_graph():
    global Z, G, N, F

    res = [[] for _ in range(Z+1)]
    order = [0] * (Z+1)

    for n in range(1, N+1):
        u = F[n]

        for x in G[n]:
            v = F[x]

            if u == v: continue

            res[u].append(v)
            order[v] += 1

    return res, order


def topology_sort(graph, order):
    global Z, N

    q = deque([])
    cmp = 1

    for idx in range(1, Z+1):
        if not order[idx]: q.append(idx)

    if len(q) > 1:
        print(0)
        return

    res = q[0]
    while q:
        if len(q) > 1:
            print(0)
            return

        n = q.popleft()

        for x in graph[n]:
            order[x] -= 1

            if not order[x]:
                q.append(x)
                cmp += 1

    if cmp == Z:
        ans = []

        for idx in range(1, N+1):
            if F[idx] == res:
                ans.append(idx)

        print(len(ans))
        print(*ans)
        return
    else:
        print(0)
        return


def solve():
    global V, F, O, S, G, Z, N

    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    V = [0] * (N+1)
    F = [0] * (N+1)
    O = 0
    Z = 0
    S = []

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)

    for n in range(1, N+1):
        if not V[n]: scc(n)

    graph, order = generate_graph()

    topology_sort(graph, order)

    return


if __name__ == "__main__":
    solve()