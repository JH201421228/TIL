# import sys
from collections import deque
# sys.stdin = open('input.txt')

Test = int(input())

for test in range(Test):
    N, M = map(int, input().split())
    que = deque(list(map(int, input().split())))
    for _ in range(M):
        que.append(que.popleft())
    print(f'#{test+1} {que.popleft()}')