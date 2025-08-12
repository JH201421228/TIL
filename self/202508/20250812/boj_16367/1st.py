import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


color = {'R': 1, 'B': -1}


def minor_setting(a, b):
    global G

    G[-a].append(b)
    G[-b].append(a)

    return


def setting(a, b, c, d, e, f):
    global G

    minor_setting(int(a) * color[b], int(c) * color[d])
    minor_setting(int(a) * color[b], int(e) * color[f])
    minor_setting(int(c) * color[d], int(e) * color[f])

    return


def scc(n):
    global G, O, V, F, S, cnt
    p = V[n] = O = O + 1
    S.append(n)

    for x in G[n]:
        if not V[x]: p = min(p, scc(x))
        elif not F[x]: p = min(p, V[x])

    if p == V[n]:
        cnt += 1

        while S:
            o = S.pop()
            F[o] = cnt

            if o == n: break

    return p


def set_color(n):
    global W, G

    q = deque([n])

    while q:
        n = q.popleft()
        W[n] = 1
        W[-n] = -1

        for x in G[n]:
            if not W[x]:
                q.append(x)

    return


def solve():
    global G, O, S, V, F, W, cnt
    K, N = map(int, input().split())
    G = [[] for _ in range(2*K+1)]

    for _ in range(N):
        setting(*list(input().rstrip().split()))

    V = [0] * (2*K+1)
    F = [0] * (2*K+1)
    S = []
    O = 1
    cnt = 0

    for n in range(1, 2*K+1):
        if not V[n]: scc(n)

    for n in range(1, N+1):
        if F[n] == F[-n]:
            print(-1)
            return

    W = [0] * (2*K+1)
    for n in range(1, K+1):
        if not W[n]: set_color(n)

    print(W)
    ans = ''
    for idx in range(1, K+1):
        if W[idx] == 1: ans += 'R'
        else: ans += 'B'

    print(ans)
    # 1 2 3 4 5 6 7
    # R B R R R B R
    # B R B B B R B

    # https: // www.acmicpc.net / source / 79348011
    return


if __name__ == "__main__":
    solve()