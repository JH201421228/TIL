import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100_001)
input = sys.stdin.readline


def scc(n):
    global O, cnt

    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]:
            p = min(p, scc(x))
        elif not F[x]:
            p = min(p, V[x])

    if p == V[n]:
        cnt += 1
        while S:
            out = S.pop()
            F[out] = cnt
            if n == out:
                break

    return p


N = int(input())
I = [0]
cnt = 0
Gs = [(0, 1)]

for _ in range(N):
    temp = list(map(int, input().split()))

    if temp[0] == 1:
        Gs.append((temp[1], temp[2]))
        cnt += 1
    else:
        I.append(cnt)

s, e = 1, len(I)-1

while s <= e:
    mid = (s+e) >> 1

    G = [[] for _ in range(200_001)]
    S = []
    V = [0] * 200_001
    F = [0] * 200_001
    cnt = 0
    O = 0
    S = []

    for a, b in Gs[1:I[mid]+1]:
        G[-a].append(b)
        G[-b].append(a)

    for i in range(-100_000, 100_001):
        if i and not V[i]:
            scc(i)

    for i in range(1, 100_001):
        if F[i] and F[-i] == F[i]:
            e = mid-1
            break
    else:
        s = mid+1

for _ in range(e):
    print('YES DINNER')
for _ in range(len(I)-e-1):
    print('NO DINNER')