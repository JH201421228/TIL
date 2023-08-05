import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
ans_stack = []
for test_case in range(N):

    commend = list(map(int, input().split()))

    if commend[0] == 2:
        if ans_stack:
            output = ans_stack.pop()
            print(output)
        else:
            print(-1)
    elif commend[0] == 3:
        print(len(ans_stack))
    elif commend[0] == 4:
        if ans_stack:
            print(0)
        else:
            print(1)
    elif commend[0] == 5:
        if ans_stack:
            print(ans_stack[-1])
        else:
            print(-1)
    else:
        ans_stack.append(commend[1])
