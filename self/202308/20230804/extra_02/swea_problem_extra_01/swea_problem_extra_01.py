# 고대 유적
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    N, M = map(int, input().split())
    treasure_list = [list(map(int, input().split())) for _ in range(N)]
    trans_treasure_list = [[0] * N for _ in range(M)]

    for i in range(N):
        for j in range(M):
            trans_treasure_list[j][i] = treasure_list[i][j]

    # print(trans_treasure_list)

    max_val1 = 0
    for treasure in treasure_list:
        check_plz = [0]
        for zero_or_one in treasure:
            if zero_or_one == 0:
                check_plz.append(0)
            else:
                check_plz[-1] += 1
        if max(check_plz) > max_val1:
            max_val1 = max(check_plz)

    max_val2 = 0
    for treasure in trans_treasure_list:
        check_plz = [0]
        for zero_or_one in treasure:
            if zero_or_one == 0:
                check_plz.append(0)
            else:
                check_plz[-1] += 1
        if max(check_plz) > max_val2:
            max_val2 = max(check_plz)

    if max_val1 >= max_val2:
        max_val = max_val1
    else:
        max_val = max_val2

    print(f'#{test_case+1} {max_val}')