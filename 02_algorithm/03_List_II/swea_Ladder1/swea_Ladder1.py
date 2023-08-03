import sys
sys.stdin = open('input.txt')

for test_case in range(10):
    test_num = int(input())
    raw_list = [list(map(int, input().split())) for _ in range(100)]

    while True:
        x = 0
        y = raw_list[0].index(1)
        ans = raw_list[0].index(1)
        status = 0
        while True:
            if y+1 < 100 and raw_list[x][y+1] == 1 and status != 1:
                status = -1
                y += 1
            elif 0 <= y-1 and raw_list[x][y-1] == 1 and status != -1:
                status = 1
                y -= 1
            else:
                x += 1
                status = 0
            if x == 99:
                break

        if raw_list[x][y] == 2:
            break
        else:
            raw_list[0][ans] = 0

    print(f'#{test_num} {ans}')