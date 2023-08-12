import sys
from collections import deque
# sys.stdin = open('input.txt')


def game():
    trace = [0] * 101
    trace[0]
    dice = [1, 2, 3, 4, 5, 6]
    que = deque([])
    que.append(1)

    while que:
        now = que.popleft()
        for plus in dice:
            next = now + plus
            if next <= 100 and not trace[next]:
                trace[next] = trace[now] + 1

                if next in ladder_start:
                    move = ladder_end[ladder_start.index(next)]
                    if not trace[move]:
                        trace[move] = trace[next]
                        que.append(move)
                elif next in snake_start:
                    move = snake_end[snake_start.index(next)]
                    if not trace[move]:
                        trace[move] = trace[next]
                        que.append(move)
                else:
                    que.append(next)
            if next == 100:
                return trace[100]

ladder_num, snake_num = map(int, input().split())

ladder_start = []
ladder_end = []
snake_start = []
snake_end = []

for _ in range(ladder_num):
    start, end = map(int, input().split())
    ladder_start.append(start)
    ladder_end.append(end)

for _ in range(snake_num):
    start, end = map(int, input().split())
    snake_start.append(start)
    snake_end.append(end)

print(game())