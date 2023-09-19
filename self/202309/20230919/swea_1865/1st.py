import sys
from itertools import permutations
sys.stdin = open('input.txt')


def why_do_i_make_this_func(N):
    if len(temp) == N:
        permu_list.append(temp)
        return

    for num in num_list:
        if num not in temp:
            temp.append(num)
            why_do_i_make_this_func(N)
            temp.pop()



T = int(input())
for test in range(T):
    N = int(input())
    chance_list = [list(map(int, input().split())) for _ in range(N)]
    num_list = list(range(N))
    temp = []
    permu_list = []
    # print(num_list)
    why_do_i_make_this_func(N)
    print(permu_list)
