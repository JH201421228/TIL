import sys
sys.stdin = open('input.txt')


def why_do_this(N):
    if N < 6:
        return (N - 1) // 3 + 1

    return_list = [0] * (N + 1)
    return_list[1] = 1
    return_list[2] = 1
    return_list[3] = 1
    return_list[4] = 2
    return_list[5] = 2

    for idx in range(6, N+1):
        return_list[idx] = return_list[idx - 1] + return_list[idx - 5]
    return return_list[N]




T = int(input())
for _ in range(T):
    N = int(input())
    print(why_do_this(N))