import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(200_000)


def find_scc(now):
    global val, cnt

    parent = V[now] = val = val + 1
    S.append(now)

    for nxt in G[now]:
        if not V[nxt]:
            parent = min(parent, find_scc(nxt))
        elif not F[nxt]:
            parent = min(parent, V[nxt])

    if parent == V[now]:
        cnt += 1
        while S:
            out = S.pop()
            F[out] = 1
            Gn[out] = cnt
            if out == now:
                break

    return parent


for _ in range(int(input())):
    N, M = map(int, input().split())
    P = []
    for _ in range(N):
        P.append(list(map(str, input().rstrip())))
    b_n = w_n = 0
    for i in range(N):
        for j in range(M):
            if P[i][j] == 'B':
                P[i][j] = b_n = b_n + 1

    G = [set() for _ in range(4*b_n+1)]
    V = [0] * (4*b_n+1)
    F = [0] * (4*b_n+1)
    Gn = [0] * (4*b_n+1)
    cnt = val = 0
    S = []

    # 가로방향 (n-1)*2+1 오른쪽 + // 왼쪽 -
    # 세로방향 (n-1)*2+2 아래 + // 위 -
    isPossible = True
    for i in range(N):
        for j in range(M):
            if isinstance(P[i][j], int):
                r = l = u = d = False

                if i-1 >= 0 and P[i-1][j] == 'W':
                    u = True
                if i+1 < N and P[i+1][j] == 'W':
                    d = True
                if j-1 >= 0 and P[i][j-1] == 'W':
                    l = True
                if j+1 < M and P[i][j+1] == 'W':
                    r = True

                if (not r and not l) or (not u and not d):
                    isPossible = False
                    # print('B')

                if isPossible:
                    a = (P[i][j]-1)*2+1
                    b = (P[i][j]-1)*2+2

                    if r and l:
                        G[a].add(a)
                        G[-a].add(-a)
                    elif r:
                        G[-a].add(a)
                    elif l:
                        G[a].add(-a)

                    if u and d:
                        G[b].add(b)
                        G[-b].add(-b)
                    elif d:
                        G[-b].add(b)
                    elif u:
                        G[b].add(-b)

            elif P[i][j] == 'W':
                # print('i, j', i, j)
                w_n += 1
                r = l = u = d = False

                if i-1 >= 0 and isinstance(P[i-1][j], int):
                    u = P[i-1][j]
                if i+1 < N and isinstance(P[i+1][j], int):
                    d = P[i+1][j]
                if j-1 >= 0 and isinstance(P[i][j-1], int):
                    l = P[i][j-1]
                if j+1 < M and isinstance(P[i][j+1], int):
                    r = P[i][j+1]

                if not u and not d and not l and not r:
                    isPossible = False
                    # print('W')

                if isPossible:
                    temp = []
                    if u:
                        temp.append((u-1)*2+2)
                    if d:
                        temp.append(-((d-1)*2+2))
                    if l:
                        temp.append((l-1)*2+1)
                    if r:
                        temp.append(-((r-1)*2+1))

                    # print(temp)
                    if len(temp) == 1:
                        a = temp.pop()
                        G[-a].add(a)
                    else:
                        for c in range(len(temp)-1):
                            for d in range(c+1, len(temp)):
                                a, b = temp[c], temp[d]
                                G[a].add(-b)
                                G[b].add(-a)

    if b_n*2 != w_n:
        isPossible = False

    ans_list = [0] * (2*b_n+1)
    ans = 'YES'
    if not isPossible:
        ans = 'NO'
    else:
        for idx in range(-(2*b_n), 2*b_n+1):
            if idx and not V[idx]:
                find_scc(idx)
        for idx in range(1, 2*b_n+1):
            if Gn[idx] == Gn[-idx]:
                ans = 'NO'
            elif Gn[idx] > Gn[-idx]:
                ans_list[idx] = False
            else:
                ans_list[idx] = True

    print(ans)
    # print(ans_list)
    # print(P)
    # print(G)
    # print(V)
    # print(isPossible)
    # print(b_n, w_n)
