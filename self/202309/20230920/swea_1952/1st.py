import sys
sys.stdin = open('input.txt')


T = int(input())
for test in range(T):
    cost = list(map(int, input().split()))
    day, month, three_month, year = cost
    month_info = list(map(int, input().split()))
    # print(month_info)
    # print(day, month, three_month, year)
    for idx in range(12):
        month_info[idx] = min(month_info[idx] * day, month)
    # print(month_info)
    for idx in range(1, 12):
        if idx == 1 or idx == 2:
            month_info[idx] = min(month_info[idx] + month_info[idx-1], three_month)
        # elif idx == 2:
        #     month_info[idx] = min(month_info[idx] + month_info[idx-1] + month_info[idx-2], three_month)
        else:
            month_info[idx] = min(month_info[idx] + month_info[idx-1], month_info[idx-3] + three_month)
    print(f'#{test + 1} {min(month_info[-1], year)}')