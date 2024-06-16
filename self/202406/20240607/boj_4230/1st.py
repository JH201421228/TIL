import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_scc(now):
    global cnt, val
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


while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    G = [set() for _ in range(4*N+1)]
    V = [0] * (4*N+1)
    F = [0] * (4*N+1)
    Gn = [0] * (4*N+1)
    S = []
    cnt = val = 0

    G[1].add(-1)
    G[-2].add(2)

    for i in range(1, N):
        a, b = i*2+1, i*2+2

        G[-a].add(b)
        G[-b].add(a)
        G[a].add(-b)
        G[b].add(-a)

    for _ in range(M):
        a, b = map(str, input().split())

        if a[-1] == 'h':
            a = int(a.split('h')[0])*2+1
        else:
            a = int(a.split('w')[0])*2+2

        if b[-1] == 'h':
            b = int(b.split('h')[0])*2+1
        else:
            b = int(b.split('w')[0])*2+2
        # print(a, b)
        G[-a].add(b)
        G[-b].add(a)

    for idx in range(-(2*N), 2*N+1):
        if idx and not V[idx]:
            find_scc(idx)
    ans = True
    ans_list = []
    for idx in range(1, 2*N+1):
        if Gn[idx] == Gn[-idx]:
            ans = False
        elif Gn[idx] < Gn[-idx]:
            ans_list.append(idx)

    if ans:
        temp = []
        for value in ans_list[1:]:
            if value % 2:
                temp.append(''.join((str((value-1)//2), 'h')))
            else:
                temp.append(''.join((str((value - 1) // 2), 'w')))
        print(*temp)
    else:
        print('bad luck')

    # print(G)
    # print(V)
    # print(temp)
    # print(ans_list)
    # print(ans_list)
    # print(ans)