import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
que = deque([])
for _ in range(N):

    commend = list(map(int, input().split()))

    if commend[0] == 1:
        que.appendleft(commend[1])

    elif commend[0] == 2:
        que.append(commend[1])

    elif commend[0] == 3:
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif commend[0] == 4:
        if que:
            print(que.pop())
        else:
            print(-1)

    elif commend[0] == 5:
        print(len(que))

    elif commend[0] == 6:
        if que:
            print(0)
        else:
            print(1)

    elif commend[0] == 7:
        if que:
            print(que[0])
        else:
            print(-1)

    elif commend[0] == 8:
        if que:
            print(que[-1])
        else:
            print(-1)