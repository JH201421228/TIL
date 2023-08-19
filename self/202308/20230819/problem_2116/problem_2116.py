import sys
sys.stdin = open('input.txt')


def remover(num, idx): # 주사위의 아랫면 인덱스를 넣으면 윗면의값과 옆면중 가장 큰 값을 반환
    dice = dice_list[num][:]
    if idx == 0 or idx == 5:
        next_idx = 5 - idx
        upper_val = dice[next_idx]
        dice.pop(5)
        dice.pop(0)
    elif idx == 1 or idx == 3:
        next_idx = 4 - idx
        upper_val = dice[next_idx]
        dice.pop(3)
        dice.pop(1)
    else:
        next_idx = 6 - idx
        upper_val = dice[next_idx]
        dice.pop(4)
        dice.pop(2)
    return [upper_val, max(dice)]


def find_max():
    max_val = 0
    for i in range(1, 7):
        # dice_order[i] # 몇번째 주사위인지
        # dice_list[dice_order[i]].index(i+1) # 주사위 아랫면 인덱스
        , val1 = remover(dice_order[0], dice_list[dice_order[0]].index(i))
        max_val += val1
        idx2, val2 = remover(dice_order[1], dice_list[dice_order[1]].index(idx1))
        max_val += val2
        idx3, val3 = remover(dice_order[2], dice_list[dice_order[2]].index(idx2))
        max_val += val3
        idx4, val4 = remover(dice_order[3], dice_list[dice_order[3]].index(idx3))
        max_val += val4
        idx5, val5 = remover(dice_order[4], dice_list[dice_order[4]].index(idx4))
        max_val += val5
    return max_val

def permu(dice_num):
    if len(dice_order) == dice_num:
        ans.append(find_max())
        print(ans)
        return
    for i in range(6):
        if i not in dice_order:
            dice_order.append(i)
            permu()
            dice_order.pop()


dice_num = int(input())
dice_list = [list(map(int, input().split())) for _ in range(dice_num)]
# dice link info (index) 0-5 1-3 2-4
dice_order = []
cnt = 0
ans = []
permu()

print(ans)
