import sys
sys.stdin = open('input.txt')
iuput = sys.stdin.readline
from collections import deque


N, M, K = map(int, input().split()) # M 이 0, 1이면 모등 강의동이 연결되어 있음
stones = list(map(int, input().split()))
graph = [[1]*2 for _ in range(N)] # [n][0] n-1 과의 연결 여부, [n][1] n+1 과의 연결 여부
# print(graph)
for _ in range(M):
    a, b = map(int, input().split())
    if max(a, b) == N and min(a, b) == 1:
        graph[0][0], graph[-1][1] = 0, 0
    else:
        graph[max(a, b)-1][0], graph[min(a, b)-1][1] = 0, 0
# print(graph)

def bfs(n):
    q = deque([n])
    visited[n] = 1
    cost = float('inf')
    while q:
        now = q.popleft()
        cost = min(cost, stones[now])
        prev, next = (now-1) % N, (now+1) % N
        if not visited[prev] and graph[now][0]:
            visited[prev] = 1
            q.append(prev)
        if not visited[next] and graph[now][1]:
            visited[next] = 1
            q.append(next)
    return cost

visited = [0] * N

if M == 0 or M == 1:
    print('YES')
    exit(0)

c = 0
for i in range(N):
    if not visited[i]:
        c += bfs(i)
if c <= K:
    print('YES')
else:
    print('NO')