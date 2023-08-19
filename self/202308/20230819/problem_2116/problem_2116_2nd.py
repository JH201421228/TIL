import sys
sys.stdin = open('input.txt')

dice_num = int(input())
dice_list = [list(map(int, input().split())) for _ in range(dice_num)]
print(dice_list)