import sys
from collections import deque
# sys.stdin = open('input.txt')


def idiot(N):
    que = deque([[1, 0]])
    while que:
        now = que.popleft()
        # print(now)
        next1 = [now[0], now[0]] # 클립보드 복사
        next2 = [now[0] - 1, now[1]] # 한개 지우기
        next3 = [now[0] + now[1], now[1]] # 클립보드 붙여넣기

        if now[0] == N:
            return imo_and_clip[now[0]][now[1]]
        else:
            if not imo_and_clip[next1[0]][next1[1]]:
                imo_and_clip[next1[0]][next1[1]] = imo_and_clip[now[0]][now[1]] + 1
                que.append([next1[0], next1[1]])
            if 0 <= next2[0] and not imo_and_clip[next2[0]][next2[1]]:
                imo_and_clip[next2[0]][next2[1]] = imo_and_clip[now[0]][now[1]] + 1
                que.append([next2[0], next2[1]])
            if next3[0] < 1001 and not imo_and_clip[next3[0]][next3[1]]:
                imo_and_clip[next3[0]][next3[1]] = imo_and_clip[now[0]][now[1]] + 1
                que.append([next3[0], next3[1]])


N = int(input())
imo_and_clip = [[0] * 1001 for _ in range(1001)]
imo_and_clip[1][0] = 1
print(idiot(N) - 1)