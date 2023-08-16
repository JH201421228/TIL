import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test in range(Test_Case):
    cal = list(map(str, input().split()))
    cal.pop()
    stack = []
    flag = 0
    for something in cal:
        try:
            if something == '+':
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                stack.append(pop2+pop1)
            elif something == '*':
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                stack.append(pop2 * pop1)
            elif something == '/':
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                stack.append(pop2 // pop1)
            elif something == '-':
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                stack.append(pop2 - pop1)
            else:
                stack.append(something)
        except:
            flag = 1
    if flag or not stack or len(stack) > 1:
        ans = 'error'
    else:
        ans = stack[0]
    print(f'#{test + 1} {ans}')