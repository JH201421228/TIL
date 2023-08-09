import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    stack1 = list(input())
    stack2 = []

    while stack1:
        if stack1 and stack2:
            if stack1[-1] == stack2[-1]:
                stack1.pop()
                stack2.pop()
            else:
                stack2.append(stack1.pop())

        else:
            stack2.append(stack1.pop())

    print(f'#{test_case + 1} {len(stack2)}')
