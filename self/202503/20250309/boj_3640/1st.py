import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


while True:
    try:
        V, E = map(int, input().split())
    except:
        break

    ans = 0
    G = [[] for _ in range(V+1)]
    C = [[0] * (V+1) for _ in range(V+1)]
    F = [[0] * (V+1) for _ in range(V+1)]
    D = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        a, b, c = map(int, input().split())

        G[a].append(b)
        G[b].append(a)
        C[a][b] = 1
        D[a][b] = c

    for _ in range(2):
        pre, dist, checker = [-1] * (V+1), [float("inf")] * (V+1), [0] * (V+1)
        q = deque([1])
        dist[1], checker[1] = 0, 1

        while q:
            n = q.popleft()
            checker[n] = 0

            for x in G[n]:
                if C[n][x] > F[n][x] and dist[x] > dist[n] + D[n][x]:
                    dist[x] = dist[n] + D[n][x]
                    pre[x] = n

                    if not checker[x]:
                        checker[x] = 1
                        q.append(x)

        n = V
        while n != 1:
            F[pre[n]][n] += 1
            F[n][pre[n]] -= 1
            D[n][pre[n]] = -D[pre[n]][n]
            ans += D[pre[n]][n]

            print(pre[n], n, D[pre[n]][n])

            n = pre[n]

    print(ans)