import sys
from collections import deque
sys.setrecursionlimit(3_000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(n, G, V):
    global cycle, is_cycle, cycle_n

    for x in G[n]:
        if not is_cycle:
            if not V[x]:
                V[x] = n
                dfs(x, G, V)
            elif V[n] != x:
                cycle.append(n)
                is_cycle = 1
                cycle_n = x
                return

        if is_cycle == 1:
            cycle.append(n)
            if n == cycle_n:
                is_cycle = 2
            return

        if is_cycle == 2:
            return

    return


def bfs(n, G, V, ans):
    q = deque([n])

    while q:
        n = q.popleft()

        for x in G[n]:
            if not V[x]:
                V[x] = 1
                ans[x] = ans[n] + 1
                q.append(x)

    return ans


def solve():
    global cycle, is_cycle, cycle_n

    N = int(input())
    G = [[] for _ in range(N+1)]

    for _ in range(N):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    start = None

    for n in range(1, N+1):
        if len(G[n]) == 1:
            start = n
            break

    ans = [0] * (N+1)

    if not start:
        print(*ans[1:])
        return

    cycle = []
    is_cycle = 0
    cycle_n = 0

    V = [0] * (N+1)
    V[start] = 1
    dfs(start, G, V)

    start_n = []
    is_cycle_n = [0] * (N+1)
    ans = [0] * (N+1)
    for n in cycle:
        is_cycle_n[n] = 1
        if len(G[n]) > 2:
            start_n.append(n)

    for n in start_n:
        ans = bfs(n, G, is_cycle_n, ans)

    print(*ans[1:])

    return


if __name__ == "__main__":
    solve()