import sys
sys.stdin = open('input.txt')


N = int(input())
strange_list = [N]
ans_num = 0
ans_list = []
for i in range(0, N + 1):
    strange_list = [N, i]
    while True:
        next_num = strange_list[-2] - strange_list[-1]
        if next_num >= 0:
            strange_list.append(next_num)
        else:
            break

    if len(strange_list) > ans_num:
        ans_num = len(strange_list)
        ans_list = strange_list[:]
print(ans_num)
print(*ans_list)
