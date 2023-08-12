import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


commend_num = int(input())
que = deque([])
for _ in range(commend_num):
    commend = list(map(str, input().split()))

    if commend[0] == 'push':
        que.append(int(commend[1]))

    elif commend[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif commend[0] == 'size':
        print(len(que))

    elif commend[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)

    elif commend[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)

    elif commend[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
