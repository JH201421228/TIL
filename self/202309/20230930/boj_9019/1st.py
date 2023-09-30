import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def DSLR(now_num):
    visited = [0] * 10_000
    visited[int(now_num)] = 1
    now_list = list(now_num.zfill(4))
    que = deque([(now_list, '')])
    while que:
        now, commend = que.popleft()
        next1 = deque([*now])
        next2 = deque([*now])
        next3 = deque([])
        next4 = deque([])

        next1.append(next1.popleft()) # L
        num1 = int(''.join(next1))
        if not visited[num1]:
            if num1 == ans:
                return commend + 'L'
            visited[num1] = 1
            que.append((next1, commend + 'L'))


        next2.appendleft(next2.pop()) # R
        num2 = int(''.join(next2))
        if not visited[num2]:
            if num2 == ans:
                return commend + 'R'
            visited[num2] = 1
            que.append((next2, commend + 'R'))


        num = int(''.join(now))

        num3 = (num*2) % 10_000
        next3.extend(list(str(num3).zfill(4))[:])
        if not visited[num3]:
            if num3 == ans:
                return commend + 'D'
            visited[num3] = 1
            que.append((next3, commend + 'D'))

        num4 = num
        if not num4:
            num4 = 9_999
        else:
            num4 = num - 1
        next4.extend(list(str(num4).zfill(4))[:])
        if not visited[num4]:
            if num4 == ans:
                return commend + 'S'
            visited[num4] = 1
            que.append((next4, commend + 'S'))


for _ in range(int(input())):
    num_list = list(input().split())
    ans = int(num_list[-1])
    print(DSLR(num_list[0]))


