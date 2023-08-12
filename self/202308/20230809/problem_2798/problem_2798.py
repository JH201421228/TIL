import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


num, limit_num = map(int, input().split())

card_list = list(map(int, input().split()))

N = len(card_list)
max_val = 0

for i in range(1<<N):
    check_list = []
    for j in range(N):
        if i & (1<<j):
            check_list.append(card_list[j])


    if len(check_list) == 3:
        sum_val = sum(check_list)
        if sum_val > max_val and limit_num >= sum_val:
            max_val = sum_val

print(max_val)