import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for k in range(1, N+1):
        if G[n][k]:
            if V[k]:
                continue
            V[k] = 1

            if not C[k] or B(C[k]):
                C[k] = n
                return True

    return False


N, M = map(int, input().split())
G = [[1] * (N+1) for _ in range(N+1)]

for _ in range(M):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        for i in range(1, N+1):
            if i >= temp[1] and i <= temp[2]:
                for j in range(temp[3]+1, N+1):
                    G[i][j] = 0
            else:
                G[i][temp[3]] = 0

    else:
        for i in range(1, N + 1):
            if i >= temp[1] and i <= temp[2]:
                for j in range(1, temp[3]):
                    G[i][j] = 0
            else:
                G[i][temp[3]] = 0

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