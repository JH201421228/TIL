import sys
sys.stdin = open('input.txt')
from itertools import combinations

N, sum_val = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    ans_list = combinations(numbers, i)
    for ans in ans_list:
        if sum(ans) == sum_val:
            cnt += 1
print(cnt)