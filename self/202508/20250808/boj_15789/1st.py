import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(n):
    global V, G

    res = []
    V[n] = 1
    q = deque([n])

    while q:
        n = q.popleft()
        res.append(n)

        for x in G[n]:
            if not V[x]:
                V[x] = 1
                q.append(x)


    return res


def solve():
    global V, G

    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    V = [0] * (N+1)

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    C, H, K = map(int, input().split())

    ans = len(bfs(C))
    bfs(H)

    temp = []
    for n in range(1, N+1):
        if not V[n]:
            res = bfs(n)
            temp.append([len(res), *res])

    temp.sort(reverse=True)

    for idx in range(min(K, len(temp))):
        ans += temp[idx][0]

    print(ans)

    return


if __name__ == "__main__":
    solve()