import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(cur, tar, G, V, charge, C, pride, value):
    if cur == tar:
        return min(pride, value)

    for nxt, cost in G[cur]:
        if not V[nxt] and charge+cost <= C and (not value or cost < value):
            V[nxt] = 1
            value = dfs(nxt, tar, G, V, charge+cost, C, max(pride, cost), value)
            V[nxt] = 0

    return value


def solve():
    N, M, A, B, C = map(int, input().split())

    G = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        G[u].append((v, c))
        G[v].append((u, c))

    V = [0] * (N+1)
    V[A] = 1
    ans = dfs(A, B, G, V, 0, C, 0, float("inf"))

    if ans == float("inf"): print(-1)
    else: print(ans)

    return


if __name__ == "__main__":
    solve()