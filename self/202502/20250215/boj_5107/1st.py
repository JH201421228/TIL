import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(n):
    S = [n]
    V[n] = 1

    while S:
        o = S.pop()

        for x in G[o]:
            if not V[x]:
                V[x] = 1
                S.append(x)

    return

T = 0
while True:
    N = int(input())
    if not N:
        break

    G = [[] for _ in range(N+1)]

    name_dict = {}
    cnt = 1
    for _ in range(N):
        u, v = map(str, input().rstrip().split())

        if u not in name_dict:
            name_dict[u] = cnt
            cnt += 1

        if v not in name_dict:
            name_dict[v] = cnt
            cnt += 1

        G[name_dict[u]].append(name_dict[v])

    V = [0] * (N+1)

    ans = 0
    for n in range(1, N+1):
        if not V[n]:
            ans += 1
            dfs(n)

    print(T+1, ans)
    T += 1