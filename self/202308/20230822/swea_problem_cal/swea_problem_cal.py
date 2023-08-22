import sys
sys.setrecursionlimit(15000)
sys.stdin = open('input.txt')


def some_order(N):
    if not N:
        return
    some_order(left[N])
    some_order(right[N])
    ans.append(value[N])


for test in range(10):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    value = [0] * (N+1)
    input_list = []
    for _ in range(N):
        input_list.append(list(input().split()))

    for inner_list in input_list:
        if len(inner_list) == 2:
            value[int(inner_list[0])] = int(inner_list[1])
        else:
            value[int(inner_list[0])] = inner_list[1]
            left[int(inner_list[0])] = int(inner_list[2])
            right[int(inner_list[0])] = int(inner_list[3])
    ans = []
    some_order(1)
    cal = []
    # print(ans)
    while ans:
        cal.append(ans.pop(0))

        if type(cal[-1]) == str:
            op = cal.pop(-1)
            num2 = int(cal.pop(-1))
            num1 = int(cal.pop(-1))

            if op == '+':
                cal.append(num1 + num2)
            elif op == '-':
                cal.append(num1 - num2)
            elif op == '/':
                cal.append(num1 / num2)
            elif op == '*':
                cal.append(num1 * num2)
    print(f'#{test+1} {int((cal[0]))}')

