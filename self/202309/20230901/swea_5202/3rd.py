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
        start, end = ans_list[order]
        for idx in range(start, end):
            time_line[idx] += 1
        today_is_good_day_isn_t_it(num+1, order + 1, order_num)
        for idx in range(start, end):
            time_line[idx] -= 1



T = int(input())
for test in range(T):
    order_num = int(input())
    order_info = [list(map(int, input().split())) for _ in range(order_num)]
    ans_list = []
    while order_info:
        now_start, now_end = order_info.pop()
        for start, end in order_info:
            if now_start <= start and end <= now_end:
                break
        else:
            ans_list.append([now_start, now_end])
    # print(ans_list)
    ans = 0
    order_num = len(ans_list)
    time_line = [0] * 24
    today_is_good_day_isn_t_it(0, 0, order_num)
    print(f'#{test + 1} {ans}')