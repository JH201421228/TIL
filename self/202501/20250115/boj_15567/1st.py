import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100_000)
input = sys.stdin.readline


def scc(n):
    global O, cnt

    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]:
            p = min(scc(x), p)
        elif not F[x]:
            p = min(V[x], p)

    if p == V[n]:
        cnt += 1
        while S:
            o = S.pop()
            F[o] = cnt
            if o == n:
                break

    return p


N, M = map(int, input().split())
V = [0] * (2*N+1)
F = [0] * (2*N+1)
S = []
O, cnt = 0, 0

interest = [[]]
for _ in range(N):
    interest.append(list(map(int, input().split())))

leafs = [[] for _ in range(N+1)]
prefer = [[]]
for i in range(1, N+1):
    a, b = map(int, input().split())
    prefer.append([a, b])
    leafs[a].append((i, 1))
    leafs[b].append((i, -1))

G = [[] for _ in range(2*N+1)]

for leaf in leafs:
    l = len(leaf)
    for i in range(l):
        for j in range(i+1, l):
            a_n, b_n = -leaf[i][0]*leaf[i][1], -leaf[j][0]*leaf[j][1]
            G[-a_n].append(b_n)
            G[-b_n].append(a_n)

# print(leafs)

logs = []
for _ in range(M):
    logs.append(list(map(int, input().split())))

for a, b, c in logs:
    a_frogs = leafs[a]
    b_frogs = leafs[b]

    for a_frog in a_frogs:
        for b_frog in b_frogs:
            if interest[a_frog[0]][c-1] != interest[b_frog[0]][c-1]:
                a_n, b_n = -a_frog[0]*a_frog[1], -b_frog[0]*b_frog[1]
                G[-a_n].append(b_n)
                G[-b_n].append(a_n)

for n in range(-N, N+1):
    if n and not V[n]:
        scc(n)

ans = []
for i in range(1, N+1):
    if F[i] == F[-i]:
        print("NO")
        exit(0)
    elif F[i] > F[-i]:
        ans.append((prefer[i][1], i))
    else:
        ans.append((prefer[i][0], i))

ans.sort()
print('YES')
temp = []
for a, b in ans:
    temp.append(b)
print(*temp)