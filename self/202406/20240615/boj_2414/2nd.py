import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(2_500)


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

Ve, Ho = [[0] * (M+1) for _ in range(N+1)], [[0] * (M+1) for _ in range(N+1)]
cnt_v, cnt_h = 1, 1
for j in range(1, M+1):
    for i in range(1, N+1):
        if graph[i][j] == '.':
            cnt_v += 1
        else:
            Ve[i][j] = cnt_v
    cnt_v += 1

for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == '.':
            cnt_h += 1
        else:
            Ho[i][j] = cnt_h
    cnt_h += 1

G = [[] for _ in range(cnt_v + 1)]
idx = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == '*':
            G[Ve[i][j]].append(Ho[i][j])

C = [0] * (cnt_h + 1)
ans = 0
for i in range(1, cnt_v+1):
    V = [0] * (cnt_h + 1)
    if B(i):
        ans += 1

print(ans)