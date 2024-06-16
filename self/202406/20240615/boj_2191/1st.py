import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


N, M, S, V = map(int, input().split())
mice = []
for _ in range(N):
    mice.append(tuple(map(float, input().split())))

hole = []
for _ in range(M):
    hole.append(tuple(map(float, input().split())))

G = [[] for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        if ((mice[i][0] - hole[j][0])**2 + (mice[i][1] - hole[j][1])**2)**0.5 / V <= S:
            G[i+1].append(j+1)

C = [0] * (M+1)
ans = 0
for i in range(1, N+1):
    V = [0] * (M+1)
    if not B(i):
        ans += 1

print(ans)