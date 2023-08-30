import sys
sys.stdin = open('input.txt')


def two_idiots(N):

    if N < 3:
        return N

    return_list = [0] * (N + 1)
    return_list[1] = 1
    return_list[2] = 2

    for idx in range(3, N+1):
        return_list[idx] = (return_list[idx - 1] + return_list[idx - 2]) % 15746

    return return_list[N]

N = int(input())
print(two_idiots(N))