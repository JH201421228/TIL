# 현주의 상자 바꾸기
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    box_num, try_num = map(int, input().split())
    box_list = [0]*box_num

    box_trans_info = [list(map(int, input().split())) for _ in range(try_num)]
    trans_num = 0
    for box_info in box_trans_info:
        trans_num += 1
        for point in range(box_info[0], box_info[1] + 1):
            box_list[point-1] = trans_num
    print(f'#{test_case + 1}', end= ' ')
    print(*box_list)
