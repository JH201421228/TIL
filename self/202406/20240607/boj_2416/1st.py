import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(250_000)


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


N, M = map(int, input().split())
G = [[] for _ in range(2*M + 1)]
V = [0] * (2*M + 1)
F = [0] * (2*M + 1)
Gn = [0] * (2*M + 1)
S = []
cnt = val = 0

for _ in range(N):
    temp = list(map(int, input().split()))

    if temp[1]:
        a = temp[0]
    else:
        a = -temp[0]

    if temp[3]:
        b = temp[2]
    else:
        b = -temp[2]

    G[-a].append(b)
    G[-b].append(a)

for idx in range(-M, M+1):
    if idx and not V[idx]:
        find_scc(idx)
ans = []
for idx in range(1, M+1):
    if Gn[idx] == Gn[-idx]:
        print('IMPOSSIBLE')
        exit(0)
    elif Gn[idx] > Gn[-idx]:
        ans.append(0)
    else:
        ans.append(1)
for v in ans:
    print(v)