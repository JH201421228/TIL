import sys
sys.stdin = open('input.txt')


def divide_three_parts(start, end):
    if ans_list[-1] == 1:
        print(ans_list)
        return


    while start < end//3:
        # ans_list[start:end//3] = ans_list[start] // 3
        val = ans_list[start]
        for idx in range(start, end // 3):
            ans_list[idx] = val//3
        divide_three_parts(start, end//3)
    while end//3 < end//3 * 2:
        # ans_list[end//3:end//3 * 2] = 0
        for idx in range(end // 3, end // 3 * 2):
            ans_list[idx] = 0
        divide_three_parts(end//3, end//3 * 2)
    while end//3 * 2 < end:
        # ans_list[end//3 * 2:end] = ans_list[end] // 3
        val = ans_list[end]
        for idx in range(end // 3 * 2, end):
            ans_list[idx] = val // 3
        divide_three_parts(end // 3 * 2, end)


checker = [0, 1]
while True:
    try:
        n = int(input())
        ans_list = [3**n] * (3**n)
        divide_three_parts(0, len(ans_list)-1)
    except EOFError:
        break