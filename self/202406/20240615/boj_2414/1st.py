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


N, M = map(int, input().split())
graph = [[]]
for _ in range(N):
    graph.append([0] + list(map(str, input().rstrip())))

G = [[] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == '*':
            G[i].append(j)

C = [0] * (M+1)
ans = 0
for i in range(1, N+1):
    V = [0] * (M+1)
    if B(i):
        ans += 1

print(ans)