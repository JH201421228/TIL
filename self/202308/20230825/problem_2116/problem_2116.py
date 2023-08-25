import sys
sys.stdin = open('input.txt')


dice_num = int(input())
dice_info = [list(map(int, input().split())) for _ in range(dice_num)]
# print(dice_info)
link_info = [5, 3, 4, 1, 2, 0]  # 각 인덱스와 값이 주사위의 맞은편
ans = 0
for i in range(6):
    total = 0
    dice_n = 0
    bottom_idx = i
    while True:
        if dice_n == dice_num:
            break

        now_bottom_val = dice_info[dice_n][bottom_idx]
        now_top_val = dice_info[dice_n][link_info[bottom_idx]]

        if now_bottom_val == 6 or now_top_val == 6:
            if now_top_val == 5 or now_bottom_val == 5:
                total += 4
            else:
                total += 5
        else:
            total += 6

        if dice_n + 1 < dice_num:
            next_bottom_idx = dice_info[dice_n + 1].index(now_top_val)
            bottom_idx = next_bottom_idx

        dice_n += 1
    if total > ans:
        ans = total
print(ans)
