import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline

bullet = int(input())
ans_list = []
que = deque([i for i in range(1, bullet + 1)])
rotation_num_list = list(map(int, input().split()))
num = que.popleft()
ans_list.append(num)
rotation_num = rotation_num_list[num - 1]
for j in range(len(rotation_num_list) -1):

    if rotation_num > 0:
        for i in range(rotation_num):
            if i == rotation_num - 1:
                num = que.popleft()
                ans_list.append(num)
            else:
                que.append(que.popleft())
    else:
        for i in range((-1) * rotation_num):
            if i == (-1) * rotation_num - 1:
                num = que.pop()
                ans_list.append(num)
            else:
                que.appendleft(que.pop())

    rotation_num = rotation_num_list[num - 1]

print(*ans_list)