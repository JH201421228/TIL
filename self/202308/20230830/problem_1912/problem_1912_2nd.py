import sys
sys.stdin = open('input.txt')

N = int(input())
integer_list = list(map(int, input().split()))
compare_list = [0] * N
compare_list[0] = integer_list[0]
for idx in range(1, N):
    compare_list[idx] = max(integer_list[idx], compare_list[idx - 1] + integer_list[idx])
print(max(compare_list))