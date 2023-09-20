import sys
from collections import deque

sys.stdin = open('input.txt')

def cal(N, M):

    visited = [False] * 1_000_001
    que = deque([(N, 0)])
    visited[N] = True

    while que:
        now, cnt = que.popleft()
        if now == M:
            return cnt

        next_positions = [now + 1, now - 1, now * 2, now - 10]
        for next_pos in next_positions:
            if 0 <= next_pos <= 1_000_000 and not visited[next_pos]:
                que.append((next_pos, cnt + 1))
                visited[next_pos] = True

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    result = cal(N, M)
    print(f'#{test + 1} {result}')
