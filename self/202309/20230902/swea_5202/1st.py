import sys
sys.stdin = open('input.txt')


T = int(input())
for test in range(T):
    N = int(input())
    time_info = [list(map(int, input().split())) for _ in range(N)]
    time_info.sort(key=lambda x: x[1])
    # print(time_info)
    ans = 1
    ans_list = [time_info[0]]
    for idx in range(1, N):
        if time_info[idx][0] >= ans_list[-1][1]:
            # print(time_info[idx])
            ans += 1
            ans_list.append(time_info[idx])
    print(f'#{test + 1} {ans}')