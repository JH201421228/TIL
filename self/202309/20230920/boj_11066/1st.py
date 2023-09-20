import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):
    N = int(input())
    nums_list = sorted(list(map(int, input().split())))
    print(nums_list)