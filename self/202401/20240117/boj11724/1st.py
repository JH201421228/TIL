import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bfs(n):
    q = deque([n])
    while q:
        now = q.popleft()
        for next in range(1, N+1):
            if ans_list[now][next] and not visited[next]:
                visited[next] = 1
                q.append(next)
    return

N, M = map(int, input().split())
ans_list = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    if not ans_list[i][j]:
        ans_list[i][j] = 1
        ans_list[j][i] = 1

visited = [0] * (N+1)

ans = 0

for n in range(1, N+1):
    if not visited[n]:
        visited[n] = 1
        ans += 1
        bfs(n)

print(ans)



