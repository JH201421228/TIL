import sys
sys.stdin = open('input.txt')


N = int(input())
ans_list = [0, 9]
if N < 2:
    print(ans_list[N])
else:
    for idx in range(2, N + 1):
        ans_list.append(ans_list[idx - 1] * 2 - 1)
    print(ans_list[-1])