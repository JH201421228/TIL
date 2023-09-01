import sys
sys.stdin = open('input.txt')


def today_is_good_day_isn_t_it(num, gogo, order_num):
    # print(time_line)

    if 2 in time_line:
        return

    global ans
    if num > ans:
        ans = num

    for order in range(gogo, order_num):
        start, end = order_info[order]
        for idx in range(start, end):
            time_line[idx] += 1
        today_is_good_day_isn_t_it(num+1, order + 1, order_num)
        for idx in range(start, end):
            time_line[idx] -= 1


T = int(input())
for test in range(T):
    order_num = int(input())
    order_info = [list(map(int, input().split())) for _ in range(order_num)]
    # order_info.sort()
    # print(order_info)
    time_line = [0] * 24
    check_line = [0] * 24
    plus_num = 0
    for order in order_info:
        start, end = order
        for idx in range(start, end):
            check_line[idx] += 1
    for order in order_info:
        start, end = order
        for idx in range(start, end):
            if check_line[idx] != 1:
                break
        else:
            order_info.remove(order)
            order_num -= 1
            plus_num += 1
    # print(order_info)
    # print('------------------')
    # print(check_line)
    ans = 0
    today_is_good_day_isn_t_it(0, 0, order_num)
    print(f'#{test+1} {ans + plus_num}')