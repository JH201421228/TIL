import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    q = deque([(N, 0)])
    cnt = 1
    ans = 0
    while q:
        now, time = q.popleft()
        if ans and time >= ans and not now == K:
            continue
        if now == K:
            if not ans:
                ans = time
            else:
                if ans == time:
                    cnt += 1
            continue
        if 0 <= now-1:
            q.append((now-1, time + 1))

        if now+1 <= 100_000:
            q.append((now+1, time + 1))

        if now*2 <= 100_000:
            q.append((now*2, time + 1))
    return [ans, cnt]


N, K = map(int, input().split())
ans = bfs()
for num in ans:
    print(num)