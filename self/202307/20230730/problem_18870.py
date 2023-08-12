import sys

N = int(input())
old_num_list = list(map(int, sys.stdin.readline().split()))

new_num_list = []

for i, num in enumerate(old_num_list):
    new_num_list.append([num, i])

new_num_list.sort()

ans_list = [0] * N

for i in range(1, N):

    if new_num_list[i][0] == new_num_list[i-1][0]:
        ans_list[new_num_list[i][1]] = ans_list[new_num_list[i-1][1]]

    else:
        ans_list[new_num_list[i][1]] = ans_list[new_num_list[i-1][1]] + 1

print(*ans_list)