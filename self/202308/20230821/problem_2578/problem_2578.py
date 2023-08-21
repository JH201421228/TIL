import sys
sys.stdin = open('input.txt')

bingo_list = [list(map(int, input().split())) for _ in range(5)]
order_list = []
for _ in range(5):
    order_list.extend(list(map(int, input().split())))
# print(bingo_list)
# print(order_list)
vertical = [0] * 5
horizon = [0] * 5
diagonal1 = 0
diagonal2 = 0
cnt = 0
for num in order_list:
    for i in range(5):
        for j in range(5):
            if num == bingo_list[i][j]:
                vertical[i] += 1
                horizon[j] += 1
                if i == j:
                    diagonal1 += 1
                if i + j == 4:
                    diagonal2 += 1

                if vertical[i] == 5:
                    cnt += 1
                if horizon[j] == 5:
                    cnt += 1
                if diagonal1 == 5:
                    cnt += 1
                    diagonal1 = 0
                if diagonal2 == 5:
                    cnt += 1
                    diagonal2 = 0
    if cnt >= 3:
        print(order_list.index(num) + 1)
        break
# print(vertical)
# print(horizon)
# print(diagonal1, diagonal2)