import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = graph[end][start] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][j] = 0
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = []
for i in range(1, N+1):
    for j in range(1, N+1):
        cnt = 0
        c1 = i
        c2 = j
        if c1 != c2:
            for k in range(1, N+1):
                if k != c1 and k != c2:
                    cnt += min(graph[k][c1], graph[k][c2])
        else:
            continue
        cnt *= 2
        ans.append((i,j, cnt))

ans = sorted(ans, key = lambda x: (x[2], x[0], x[1]))

city1 = ans[0][0]
city2 = ans[0][1]
time = ans[0][2]

if city1 < city2:
    print(city1, city2, time)
else:
    print(city2, city1, time)