import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    input_nums = sorted(list(map(int, input().split())))

    ans = 0
    print(input_nums)
    # while len(input_nums) > 1:
    #     num1 = input_nums.pop(0)
    #     num2 = input_nums.pop(0)
    #     ans += (num1 + num2)
    #     input_nums.append(num1+num2)
    #     input_nums.sort()
    # print(ans)