import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    result = ''
    q = deque([(start, result)])
    check_list = [start]

    while q:
        now, result = q.popleft()
        if now == end:
            return result
        if now**2 not in check_list and now**2 <= end:
            check_list.append(now**2)
            q.append((now**2, result + '*'))
        if 2*now not in check_list and 2*now <= end:
            check_list.append(2*now)
            q.append((2*now, result + '+'))
        if 1 not in check_list:
            check_list.append(1)
            q.append((1, result + '/'))
    return -1


start, end = map(int, input().split())
if start == end:
    print(0)
elif end == 1:
    print('/')
# print(start, end)
else:
    print(bfs())