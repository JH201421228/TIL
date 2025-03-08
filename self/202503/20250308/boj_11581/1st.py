import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def scc(n):
    global O, cnt
    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]:
            p = min(scc(x), p)
        elif not F[x]:
            p = min(p, V[x])

    if p == V[n]:
        cnt += 1
        while S:
            o = S.pop()
            F[o] = cnt
            if o == n:
                break

    return p


N = int(input())
G = [[] for _ in range(N+1)]
V = [0] * (N+1)
F = [0] * (N+1)
S = []
O, cnt = 0, 0

for i in range(N-1):
    input()
    temp = list(map(int, input().split()))
    for x in temp:
        G[i+1].append(x)

scc(1)

for idx in range(1, N):
    if F[idx] and idx in G[idx]:
        print("CYCLE")
        exit(0)

if O == cnt:
    print("NO CYCLE")
else:
    print("CYCLE")