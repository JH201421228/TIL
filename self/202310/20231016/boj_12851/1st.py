import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    q = deque([N])
    ans = 0
    cnt = 0
    while q:
        now = q.popleft()
        if 0 <= now-1 and not visited[now-1]:
            visited[now-1] = 1
            q.append(now-1)
            if now-1 == K:
                ans += 1
        if now+1 <= 100_000 and not visited[now+1]:
            visited[now+1] = 1
            q.append(now+1)
            if now+1 == K:
                ans += 1
        if now*2 <= 100_000 and not visited[now*2]:
            visited[now*2] = 1
            q.append(now*2)
            if now*2 == K:
                ans += 1
        cnt += 1
        if ans:
            break
    return [cnt, ans]


N, K = map(int, input().split())
visited = [0] * 100_001
visited[N] = 1
print(bfs())