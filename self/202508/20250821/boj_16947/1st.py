import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(G, N, n, ans, cross):
    V = [0] * (N+1)
    V[n] = 1
    S = [n]

    while True:
        n = S[-1]
        for x in G[n]:
            if not V[x]:
                if not cross[x]:
                    V[x] = 1
                    S.append(x)
                else:
                    cnt = 0
                    while S:
                        cnt += 1
                        o = S.pop()
                        ans[o] = cnt
                    return ans

    return


def solve():
    N = int(input())

    G = [[] for _ in range(N+1)]

    for _ in range(N):
        u, v = map(int, input().split())

        G[u].append(v)
        G[v].append(u)

    link_count = {}

    for n in range(1, N+1):
        if len(G[n]) in link_count:
            link_count[len(G[n])].append(n)
        else:
            link_count[len(G[n])] = [n]

    cross = [0] * (N+1)
    start = []
    for k, v in link_count.items():
        if k >= 3:
            for n in v:
                cross[n] = 1
        elif k == 1:
            for n in v:
                start.append(n)

    ans = [0] * (N+1)
    for n in start:
        ans = dfs(G, N, n, ans, cross)

    # print(cross)
    # print(start)
    #
    # print(link_count)

    print(*ans[1:])

    return


if __name__ == "__main__":
    solve()