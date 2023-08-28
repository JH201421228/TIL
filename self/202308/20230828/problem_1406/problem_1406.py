import sys
from collections import deque
# sys.stdin = open('input.txt')


string1 = deque(list(map(str, input())))
string2 = deque([])
commend_num = int(input())
for _ in range(commend_num):
    commend = list(map(str, input().split()))
    if commend[0] == 'L':
        if string1:
            string2.appendleft(string1.pop())
    elif commend[0] == 'D':
        if string2:
            string1.append(string2.popleft())
    elif commend[0] == 'B':
        if string1:
            string1.pop()
    else:
        string1.append(commend[1])
string1.extend(string2)
print(''.join(string1))