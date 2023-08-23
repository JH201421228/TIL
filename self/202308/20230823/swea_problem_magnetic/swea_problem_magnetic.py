import sys
sys.stdin = open('input.txt')

for test in range(10):
    N = int(input())
    magnetic_filed = [list(map(int, input().split())) for _ in range(N)]
    # print(magnetic_filed)
    # 위 N 1, 아래 S 2,
    cnt = 0
    for i in range(100):
        status = 0 # 시작 상태
        for j in range(100):
            N_S = magnetic_filed[j][i]
            if N_S == 1: # N극을 만나면
                status = 1 # N극을 만난 상태
            elif N_S == 2 and status == 1: # N극을 만난 상태에서 S극을 만나면
                status = 2 # N극을 만난 후 S극을 만난 상태

            if status == 2:
                cnt += 1
                status = 0
    print(f'#{test + 1} {cnt}')