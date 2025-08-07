import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(n, l, r, flag):
    global cnt, V, N, G

    cnt += 1
    V[n] = 1

    for x in range(N):
        if flag:
            if not V[x] and l <= G[n][x] <= r: dfs(x, l, r, flag)
        else:
            if not V[x] and l <= G[x][n] <= r: dfs(x, l, r, flag)


def checker(l, r):
    global cnt, V, N

    V = [0] * N
    cnt = 0
    dfs(0, l, r, 0)
    if cnt != N: return False

    V = [0] * N
    cnt = 0
    dfs(0, l, r, 1)
    return cnt == N



def solve():
    global N, G

    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    weights = set()
    for i in range(N):
        for j in range(N):
            weights.add(G[i][j])
    weights = list(weights)
    weights.sort()

    interval = float("inf")
    s = 0
    for e in range(len(weights)):
        while s <= e:
            if checker(weights[s], weights[e]):
                interval = min(interval, weights[e] - weights[s])
                s += 1
            else: break

    print(interval)

    return


if __name__ == "__main__":
    solve()