import sys
sys.stdin = open('input.txt')


dice_num = int(input())
dice_info = [list(map(int, input().split())) for _ in range(dice_num)]
print(dice_info)
link_info = [5, 3, 4, 1, 2, 0]  # 각 인덱스와 값이 주사위의 맞은편
for i in range(6):
    dice_n = 0
    bottom_idx = i
    while True:
        dice_num += 1

        if dice_n == dice_num:
            break
