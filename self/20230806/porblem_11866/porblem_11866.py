import sys
# sys.stdin = open('input.txt')
from collections import deque

people_num, remove_num = map(int, input().split())

que = deque([i for i in range(1, people_num + 1)])
que2 = deque([])
ans_list= []
turn = 0
while len(ans_list) < people_num:
    if turn == remove_num - 1:
        turn = 0
        ans_list.append(que.popleft())
    else:
        que.append(que.popleft())
        turn += 1

ans_list_str = [str(i) for i in ans_list]

print('<', end='')
for i in ans_list:
    if i != ans_list[-1]:
        print(i, ',', end=' ', sep='')
    else:
        print(i, '>', sep='')