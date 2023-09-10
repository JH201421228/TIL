import sys
sys.stdin = open('input.txt')


def low_cost(house_num):
    ans_list = [[min(cost_list[0]), cost_list[0].index(min(cost_list[0]))]]
    if house_num == 1:
        return ans_list[house_num - 1]

    for idx in range(1, house_num):
        ans_list.append([])


N = int(input())
cost_list = [list(map(int, input().split())) for _ in range(N)]
print(cost_list)