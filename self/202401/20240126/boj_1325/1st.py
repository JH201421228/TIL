import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(n):

    q = deque([n])
    visited = [0] * (N+1)
    visited[n] = 1

    ans = 0

    while q:
        now = q.popleft()
        ans += 1
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
    return ans


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    next, now = map(int, input().split())
    graph[now].append(next)

ans_list = [0]

for i in range(1, N+1):
    ans_list.append(bfs(i))

max_num = max(ans_list)

for i in range(1, N+1):
    if ans_list[i] == max_num:
        print(i, end=' ')
