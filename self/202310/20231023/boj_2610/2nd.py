import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 가운데 값을 조회하는 재귀 함수 만들기
# 조회하면서 visited함수 만들고
# 몇개의 파티가 있는지 세면


def party_maker(n):
    ans = [n]
    visit[n] = 1
    stack = [n]
    while stack:
        now = stack.pop()
        for next in range(1, N+1):
            if graph[now][next] and not visit[next]:
                visit[next] = 1
                stack.append(next)
                ans.append(next)
    return ans


N = int(input())
M = int(input())

graph = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = graph[end][start] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][i] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0

visit = [0] * (N+1)
ans = []
for i in range(1, N+1):
    if not visit[i]:
        ans.append(party_maker(i))

print(len(ans))
<<<<<<< HEAD
ans_list = []
=======
>>>>>>> 40c748c092dc8a38b4d611c4e02b545d680cdf24
for inner in ans:
    temp = []
    for num in inner:
        temp.append(max(graph[num][1:]))
    if len(temp) > 1:
<<<<<<< HEAD
        ans_list.append(inner[temp.index(min(temp))])
    else:
        ans_list.append(*inner)

ans_list.sort()
for num in ans_list:
    print(num)
=======
        print(inner[temp.index(min(temp))])
    else:
        print(*inner)
>>>>>>> 40c748c092dc8a38b4d611c4e02b545d680cdf24
