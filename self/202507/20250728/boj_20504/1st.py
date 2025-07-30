import sys
sys.setrecursionlimit(200_000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def scc(n):
    global G, F, V, O, S, C

    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]: p = min(p, scc(x))
        elif not F[x]: p = min(p, V[x])

    if p == V[n]:
        C += 1

        while S:
            o = S.pop()
            F[o] = C

            if o == n: break

    return p


def solve():
    global G, F, V, O, S, C

    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    V = [0] * (N+1)
    F = [0] * (N+1)
    O = 0
    S = []
    C = 0

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)

    for n in range(1, N+1):
        if not V[n]: scc(n)

    parent = {i: [] for i in range(1, C+1)}
    for n in range(1, N+1):
        for x in G[n]:
            if F[n] != F[x]:
                parent[F[x]].append(F[n])

    target_cycles = {i: False for i, v in parent.items() if not v}

    for _ in range(int(input())):
        n = int(input())
        if F[n] in target_cycles: target_cycles[F[n]] = True

    for k, v in target_cycles.items():
        if not v:
            print(-1)

            return

    print(len(target_cycles))

    return


if __name__ == "__main__":
    solve()