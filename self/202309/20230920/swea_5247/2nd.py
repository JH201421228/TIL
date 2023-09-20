import sys
sys.stdin = open('input.txt')
from collections import deque


def cal():

    while que:
        now, cnt = que.popleft()
        if now == M:
            return cnt
        else:
            if now:
                next_val = [now + 1, now - 1, now * 2, now - 10]
            else:
                next_val = [now + 1]

            for next in next_val:
                if 0 <= next <= 1_000_000 and not check_list[next]:
                    check_list[next] = 1
                    que.append([next, cnt + 1])


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    check_list = [0] * 1_000_001
    check_list[N] = 1
    que = deque([[N, 0]])
    print(f'#{test + 1} {cal()}')