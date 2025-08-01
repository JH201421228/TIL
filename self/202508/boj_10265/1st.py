import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def scc(n):
    global G, V, F, S, O, C, U

    p = V[n] = O = O + 1
    S.append(n)

    x = G[n]
    if not V[x]: p = min(p, scc(x))
    elif not F[x]: p = min(V[x], p)

    if p == V[n]:
        C += 1

        while S:
            o = S.pop()
            F[o] = C
            U[C] += 1

            if o == n:
                break

    return p


def solve():
    global G, V, F, S, O, C, U

    N, K = map(int, input().split())
    G = [0] + list(map(int, input().split()))
    V = [0] * (N+1)
    F = [0] * (N+1)
    S = []
    O = 0
    C = 0
    U = [0] * (N+1)

    for n in range(1, N+1):
        if not V[n]: scc(n)

    cycle_parent = [[] for _ in range (C+1)]
    cycle_child = [[] for _ in range (C+1)]

    for n in range(1, N+1):
        if F[n] != F[G[n]]:
            cycle_parent[F[G[n]]].append(F[n])
            cycle_child[F[n]].append(F[G[n]])

    dp = [0] * (K+1)
    dp[0] = 1
    for x in range(1, C+1):
        if not cycle_child[x]:
            temp = []
            q = deque([x])

            while q:
                n = q.popleft()
                temp.append(n)

                for nxt in cycle_parent[n]:
                    q.append(nxt)

            dp_temp = [*dp]
            for n in range(U[temp[0]], U[temp[0]] + len(temp)):
                for idx in range(K):
                    if dp[idx] and idx + n < K+1:
                        dp_temp[idx+n] = 1

            dp = dp_temp

    ans = K
    while ans:
        if dp[ans]:
            break
        ans -= 1

    print(ans)
    return


if __name__ == "__main__":
    solve()