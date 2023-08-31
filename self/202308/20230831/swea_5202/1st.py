import sys
sys.stdin = open('input.txt')


def problem(first, N, now_num):

    if 2 in time_line:
        # print('d')
        return

    global max_num
    if now_num > max_num:
        max_num = now_num
        # print('max')

    for idx in range(first, N):
        start = time_info[idx][0]
        end = time_info[idx][1]
        for time in range(start, end):
            time_line[time] += 1
        problem(first + 1, N, now_num + 1)

        for time in range(start, end):
            time_line[time] -= 1


T = int(input())
for test in range(T):
    N = int(input()) # N: 신청서
    time_info = [list(map(int, input().split())) for _ in range(N)]
    time_line = [0] * 24
    max_num = 0
    # print(time_info)
    problem(0, N, 0)
    print(f'#{test+1} {max_num}')