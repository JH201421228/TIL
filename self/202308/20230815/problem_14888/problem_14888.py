import sys
sys.stdin = open('input.txt')

def operators_func(N, arr, numbers):
    if len(arr) == N-1:
        # print(arr)
        global min_val, max_val
        nums = numbers[:]
        for i in range(N-1):
            if arr[i] == '+':
                nums[i + 1] = nums[i] + nums[i + 1]
            elif arr[i] == '-':
                nums[i + 1] = nums[i] - nums[i + 1]
            elif arr[i] == '*':
                nums[i + 1] = nums[i] * nums[i + 1]
            elif arr[i] == '/':
                if nums[i] < 0:
                    nums[i + 1] = -(-nums[i] // nums[i + 1])
                else:
                    nums[i + 1] = nums[i] // nums[i + 1]
        if nums[-1] > max_val:
            max_val = nums[-1]
        if nums[-1] < min_val:
            min_val = nums[-1]
        return

    for i in range(N-1):
        if not checker[i]:
            checker[i] = 1
            arr.append(operators[i])
            operators_func(N, arr, numbers)
            arr.pop()
            checker[i] = 0


N = int(input())
numbers = list(map(int, input().split()))
operator_info = list(map(int, input().split()))
operator_appendix = ['+', '-', '*', '/']
operators = []
for i in range(4):
    if operator_info[i]:
        for _ in range(operator_info[i]):
            operators.append(operator_appendix[i])
ans = []
checker = [0] * N
max_val = -1000000000
min_val = 1000000000
operators_func(N, ans, numbers)
print(max_val)
print(min_val)