import sys
from collections import deque
# sys.stdin = open('input.txt')


def finder(N, K):
    trace = [0] * 100001
    trace[N] = 1
    que = deque([])
    que.append(N)

    while que:
        now = que.popleft()
        if now == K:
            return 0
        delta = [-1, 1, now]
        for dx in delta:
            if 0 <= now+dx < 100001 and not trace[now+dx]:
                trace[now+dx] = trace[now] + 1
                que.append(now+dx)
                if now+dx == K:
                    return trace[now+dx] - 1


N, K = map(int, input().split())
print(finder(N, K))