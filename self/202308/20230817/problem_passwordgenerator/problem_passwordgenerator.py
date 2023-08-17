# import sys
from collections import deque
# sys.stdin = open('input.txt')

for _ in range(10):
    test_num = int(input())
    password_maker = deque(list(map(int, input().split())))
    # print(password_maker)

    num = 1
    while True:
        minus = num%5
        if minus:
            this_num = password_maker.popleft() - minus
            if this_num > 0:
                password_maker.append(this_num)
            else:
                password_maker.append(0)
                break
        else:
            this_num = password_maker.popleft() - 5
            if this_num > 0:
                password_maker.append(this_num)
            else:
                password_maker.append(0)
                break
        num += 1
    print(f'#{test_num}', end=' ')
    print(*password_maker)