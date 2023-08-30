import sys
sys.stdin = open('input.txt')

#
# def haha():
#     pass


N = int(input())
integer_list = list(map(int, input().split()))
# print(integer_list)
max_val = max(integer_list)
ans_val = 0
if N > 1:
    for i in range(1, N):
        now_val = sum(integer_list[:i])
        for j in range()