import sys
sys.stdin = open('input.txt')
from itertools import permutations


T = int(input())
for test in range(T):
    N = int(input())
    charge_list = [list(map(int, input().split())) for _ in range(N)]
    for_ans = list(permutations(list(range(1, N)), N - 1))
    # print(for_ans)
    min_val = 50*99
    ans = 0
    for inner in for_ans:
        total = charge_list[0][inner[0]] + charge_list[inner[-1]][0]
        for idx in range(N-2):
            total += charge_list[inner[idx]][inner[idx + 1]]
            # if total > min_val:
            #     break
        # total += charge_list[inner[-1]][inner[0]]
        if total < min_val:
            min_val = total
            # print(inner)
    print(f'#{test+1} {min_val}')

