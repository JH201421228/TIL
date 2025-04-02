import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def fee(T, S, F):
    if T > S:
        if (T-S)**2 > F:
            return F
        else:
            return (T-S)**2
    else:
        return 0


def solve():
    N = int(input())
    time_in = list(map(int, input().split()))
    time_out = list(map(int, input().split()))
    T = int(input())
    FF = int(input())

    ans_list = []

    src, sink = 2*N+1, 2*N+2

    G = [[] for _ in range(2*N+3)]
    D = [[0] * (2*N+3) for _ in range(2*N+3)]
    D_reverse = [[0] * (2*N+3) for _ in range(2*N+3)]
    F = [[0] * (2*N+3) for _ in range(2*N+3)]
    C = [[0] * (2*N+3) for _ in range(2*N+3)]

    for i in range(N):
        u = i+1
        G[src].append(u)
        G[u].append(src)
        C[src][u] = 1

        G[u+N].append(sink)
        G[sink].append(u+N)
        C[u+N][sink] = 1

        for j in range(N):
            v = N+j+1

            if time_out[j] - time_in[i] > 0:
                f = fee(T, time_out[j] - time_in[i], FF)
                G[u].append(v)
                G[v].append(u)
                C[u][v] = 1
                D[u][v] = f
                D_reverse[u][v] = -f
                D[v][u] = -f
                D_reverse[v][u] = f

    ans = 0
    isPossible = True

    for _ in range(N):
        pre = [-1] * (2*N+3)
        dist = [float("inf")] * (2*N+3)
        checker = [0] * (2*N+3)
        q = deque([src])
        checker[src] = 1
        dist[src] = 0

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

        if pre[sink] == -1:
            isPossible = not isPossible
            break

        n = sink
        while n != src:
            F[pre[n]][n] += 1
            F[n][pre[n]] -= 1
            ans += D[pre[n]][n]

            n = pre[n]

    if isPossible:
        ans_list.append(ans)
    else:
        print(-1)
        return


    F = [[0] * (2*N+3) for _ in range(2*N+3)]

    ans = 0

    for _ in range(N):
        pre = [-1] * (2*N+3)
        dist = [float("inf")] * (2*N+3)
        checker = [0] * (2*N+3)
        q = deque([src])
        checker[src] = 1
        dist[src] = 0

        while q:
            n = q.popleft()
            checker[n] = 0

            for x in G[n]:
                if C[n][x] > F[n][x] and dist[x] > dist[n] + D_reverse[n][x]:
                    dist[x] = dist[n] + D_reverse[n][x]
                    pre[x] = n

                    if not checker[x]:
                        checker[x] = 1
                        q.append(x)

        if pre[sink] == -1: break

        n = sink
        while n != src:
            F[pre[n]][n] += 1
            F[n][pre[n]] -= 1
            ans += D_reverse[pre[n]][n]

            n = pre[n]

    ans_list.append(-ans)

    print(*ans_list)


if __name__ == "__main__":
    solve()