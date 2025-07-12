import sys
sys.setrecursionlimit(100_000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def scc(n):
    global O, G, V, F, S, cnt

    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]: p = min(p, scc(x))
        elif not F[x]: p = min(p, V[x])

    if p == V[n]:
        cnt += 1

        while S:
            o = S.pop()
            F[o] = cnt

            if o == n: break

    return p


def solve():
    global O, G, V, F, S, cnt

    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    V = [0] * (N+1)
    F = [0] * (N+1)
    O = 0
    S = []
    cnt = 0

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)

    for n in range(1, N+1):
        if not V[n]: scc(n)

    connection = {n: [] for n in set(F[1:])}

    for n in range(1, N+1):
        for x in G[n]:
            if F[x] != F[n]: connection[F[x]].append(F[n])

    ans = 0
    for k, v in connection.items():
        if not v: ans += 1

    print(ans)

    return


if __name__ == "__main__":
    solve()