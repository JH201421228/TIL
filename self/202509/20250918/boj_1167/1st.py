import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(G, n, N):
    V = [0] * (N+1)
    q = deque([(n, 0)])
    V[n] = 1

    node, dist = 0, 0

    while q:
        n, d = q.popleft()

        for x, xd in G[n]:
            if not V[x]:
                V[x] = 1
                q.append((x, d+xd))

                if d+xd > dist:
                    dist = d+xd
                    node = x

    return node, dist


def solve():
    N = int(input())
    G = [[] for _ in range(N+1)]

    for _ in range(N):
        temp = list(map(int, input().split()))
        u = temp[0]
        idx = 1

        while True:
            if temp[idx] == -1: break

            G[u].append((temp[idx], temp[idx+1]))
            idx += 2

    print(bfs(G, bfs(G, 1, N)[0], N)[1])

    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()