import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(7_500)


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


D = dict()
cnt = 0
N = int(input())
G = [[] for _ in range(N+1)]
I = [0] * (N+1)
for i in range(1, N+1):
    a, b = map(int, input().split())
    I[i] = (a, b)

    if a+b in D:
        G[i].append(D[a+b])
    else:
        D[a+b] = cnt = cnt + 1
        G[i].append(D[a + b])

    if a-b in D:
        G[i].append(D[a-b])
    else:
        D[a-b] = cnt = cnt + 1
        G[i].append(D[a - b])

    if a*b in D:
        G[i].append(D[a*b])
    else:
        D[a*b] = cnt = cnt + 1
        G[i].append(D[a * b])

T, C = [0] * (cnt+1), [0] * (cnt+1)
for k, v in D.items():
    T[v] = k

isPossible = True
for i in range(1, N+1):
    V = [0] * (cnt+1)
    if not B(i):
        print('impossible')
        exit(0)

ans = [0] * (N+1)
for i in range(1, cnt+1):
    if C[i]:
        a, b = I[C[i]]
        c = T[i]
        if a + b == c:
            ans[C[i]] = f'{a} + {b} = {c}'
        elif a - b == c:
            ans[C[i]] = f'{a} - {b} = {c}'
        else:
            ans[C[i]] = f'{a} * {b} = {c}'

for v in ans[1:]:
    print(v)