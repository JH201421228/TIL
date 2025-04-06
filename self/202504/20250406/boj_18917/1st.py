import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

sum_res, xor_res = 0, 0

for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        sum_res += temp[1]
        xor_res ^= temp[1]
    elif temp[0] == 2:
        sum_res -= temp[1]
        xor_res ^= temp[1]
    elif temp[0] == 3:
        print(sum_res)
    else:
        print(xor_res)