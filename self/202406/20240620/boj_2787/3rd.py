import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in Ga[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


N, M = map(int, input().split())
G, Ga = [[1] * (N+1) for _ in range(N+1)], [[] for _ in range(N+1)]
MA, MI = [N] * (N+1), [1] * (N+1)

for _ in range(M):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        for i in range(1, N+1):
            if i >= temp[1] and i <= temp[2]:
                MA[i] = min(MA[i], temp[3])
            else:
                G[i][temp[3]] = 0

    else:
        for i in range(1, N + 1):
            if i >= temp[1] and i <= temp[2]:
                MI[i] = max(MI[i], temp[3])
            else:
                G[i][temp[3]] = 0

for i in range(1, N+1):
    for j in range(MI[i], MA[i]+1):
        if G[i][j]:
            Ga[i].append(j)

C = [0] * (N+1)
isPossible = True
for i in range(1, N+1):
    V = [0] * (N+1)
    if not B(i):
        isPossible = False
        break

if isPossible:
    ans = [0] * (N+1)
    for i in range(1, N+1):
        ans[C[i]] = i
    print(*ans[1:])
else:
    print(-1)