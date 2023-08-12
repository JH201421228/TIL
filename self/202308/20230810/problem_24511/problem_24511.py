import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline

queuestack_size = int(input())
que_or_stack = list(map(int, input().split())) # 0 = queue, 1 = stack
queuestack = list(map(int, input().split()))
input_num = int(input())
elements_list = list(map(int, input().split()))

deque = deque([])

for i in range(queuestack_size):
    if not que_or_stack[i]:
        deque.append(queuestack[i])

else:
    if not deque:
        print(*elements_list)
        sys.exit()

for i in range(input_num):
    deque.appendleft(elements_list[i])
    print(deque.pop(), end= ' ')