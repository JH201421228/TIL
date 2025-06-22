import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(n, cnt, arr, G):
    q = deque([n])
    arr[n] = cnt

    while q:
        n = q.popleft()

        for x in G[n]:
            if not arr[x]:
                arr[x] = cnt
                q.append(x)

    return


def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    arr = [0] * (N+1)
    cnt = 0

    for n in range(1, N+1):
        if not arr[n]:
            cnt += 1
            bfs(n, cnt, arr, G)

    order = list(map(int, input().split()))

    ans = 0
    for idx in range(1, N):
        if arr[order[idx-1]] != arr[order[idx]]: ans += 1

    print(ans)

    return


if __name__ == "__main__":
    solve()