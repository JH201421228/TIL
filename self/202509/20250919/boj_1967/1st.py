import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(G, n, N):
    V = [0] * (N+1)
    V[n] = 1
    q = deque([(n, 0)])

    cur, curd = n, 0

    while q:
        n, nd = q.popleft()

        for x, xd in G[n]:
            if not V[x]:
                V[x] = 1
                q.append((x, nd+xd))

                if nd+xd > curd:
                    cur = x
                    curd = nd+xd

    return cur, curd


def solve():
    N = int(input())

    G = [[] for _ in range(N+1)]

    for _ in range(N-1):
        u, v, d = map(int, input().split())
        G[u].append((v, d))
        G[v].append((u, d))

    print(bfs(G, bfs(G, 1, N)[0], N)[1])

    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()