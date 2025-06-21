import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dik(A, B, N, pride, charge, G):
    hq = [(0, A)]
    distance = [float("inf")] * (N+1)
    distance[A] = 0

    while hq:
        dist, cur = heapq.heappop(hq)

        for x, cost in G[cur]:
            if cost <= pride and dist+cost <= charge and dist+cost < distance[x]:
                distance[x] = dist+cost
                heapq.heappush(hq, (dist+cost, x))

    if distance[B] == float("inf"): return False
    return True


def solve():
    N, M, A, B, C = map(int, input().split())
    G = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))

    s, e = 1, 20

    while s <= e:
        mid = (s+e)>>1

        if dik(A, B, N, mid, C, G): e = mid-1
        else: s = mid+1

    if s > 20: print(-1)
    else: print(s)

    return


if __name__ == "__main__":
    solve()