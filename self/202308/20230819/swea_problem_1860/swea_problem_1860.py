import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    N, M, K = map(int, input().split()) # N 사람 수, M 초의 시간동안 K개의 붕어빵 만듦
    customer = list(map(int, input().split()))
    time_line = [0] * 11112
    for idx in customer:
        time_line[idx] = -1
    for idx in range(1, 11112):
        if not idx % M:
            time_line[idx] += K
    ans = 0
    for num in time_line:
        ans += num
        if ans < 0:
            print(f'#{test + 1} Impossible')
            break
    else:
        print(f'#{test + 1} Possible')
