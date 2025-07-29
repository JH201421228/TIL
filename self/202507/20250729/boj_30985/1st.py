import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dijkstra(G, N, s):
    dist = [float("inf")] * (N+1)
    dist[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))

    while hq:
        n_d, n = heapq.heappop(hq)

        if dist[n] < n_d: continue

        for x, x_d in G[n]:
            d = n_d + x_d
            if d < dist[x]:
                dist[x] = d
                heapq.heappush(hq, (d, x))

    return dist


def solve():
    N, M, K = map(int, input().split())
    G = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v, c = map(int, input().split())
        G[u].append((v, c))
        G[v].append((u, c))

    dists = [dijkstra(G, N, 1), dijkstra(G, N, N)]
    cost = tuple(map(int, input().split()))

    ans = float("inf")

    for idx in range(1, N+1):
        if cost[idx-1] != -1:
            ans = min(dists[0][idx] + dists[1][idx] + (K-1)*cost[idx-1], ans)

    if ans != float("inf"): print(ans)
    else: print(-1)

    return


if __name__ == "__main__":
    solve()