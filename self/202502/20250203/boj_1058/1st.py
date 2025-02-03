import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(n):
    S = []
    S.append(n)
    V[n] = 1

    res = 0

    while S:
        o = S.pop()
        for x in G[o]:
            if not V[x]:
                V[x] = V[o] + 1
                if V[x] < 3:
                    S.append(x)
                res += 1

    return res


N = int(input())
R = [list(input().rstrip()) for _ in range(N)]

G = [[] for _ in range(N+1)]
for i in range(N):
    for j in range(i+1, N):
        if R[i][j] == 'Y':
            G[i+1].append(j+1)
            G[j+1].append(i+1)

ans = 0


for i in range(1, N+1):
    V = [0] * (N + 1)
    ans = max(ans, dfs(i))

print(ans)