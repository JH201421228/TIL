import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def DSLR(now_num):
    visited = [0] * 10_000
    visited[now_num] = 1

    que = deque([(now_num, '')])
    while que:
        now, commend = que.popleft()

        num1 = now // 1_000 + (now % 1_000) * 10
        if not visited[num1]:
            if num1 == ans:
                return commend + 'L'
            visited[num1] = 1
            que.append((num1, commend + 'L'))



        num2 = now // 10 + (now % 10) * 1_000
        if not visited[num2]:
            if num2 == ans:
                return commend + 'R'
            visited[num2] = 1
            que.append((num2, commend + 'R'))

        num3 = (now*2) % 10_000
        if not visited[num3]:
            if num3 == ans:
                return commend + 'D'
            visited[num3] = 1
            que.append((num3, commend + 'D'))

        num4 = now
        if not num4:
            num4 = 9_999
        else:
            num4 = now - 1
        if not visited[num4]:
            if num4 == ans:
                return commend + 'S'
            visited[num4] = 1
            que.append((num4, commend + 'S'))


for _ in range(int(input())):
    num_list = list(map(int, input().split()))
    ans = num_list[-1]
    print(DSLR(num_list[0]))



