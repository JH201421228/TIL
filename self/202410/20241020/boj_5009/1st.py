import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def graph(t):
    global N

    for i in range(1, N+1):
        for idx in range(t, N-1):
            # i, prefer[i][idx]
            a, b = i, prefer[i][idx]
            if cur[a] == cur[b]:
                G[a].append(-b)
                G[b].append(-a)
                G[-a].append(b)
                G[-b].append(a)
            elif (cur[a]+1) % 3 == (cur[b]+2) % 3:
                G[a].append(b)
                G[-b].append(-a)
            else:
                G[-a].append(-b)
                G[b].append(a)

def scc(n):
    global cnt, O

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
cur = [0]
prefer = [[]]

for _ in range(N):
    temp = list(map(int, input().split()))
    cur.append(temp[0])
    prefer.append(temp[1:])

s, e = 0, N
while s <= e:
    mid = (s+e) >> 1

    G = [[] for _ in range(2*N+1)]
    V = [0] * (2*N+1)
    F = [0] * (2*N+1)
    S = []
    O = 0
    cnt = 0

    graph(mid)

    for i in range(-N, N+1):
        if i and not V[i]:
            scc(i)

    for i in range(1, N+1):
        if F[-i] == F[i]:
            s = mid + 1
            break
    else:
        e = mid - 1

print(s)