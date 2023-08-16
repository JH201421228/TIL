import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    N = int(input())
    inputs = input()
    stack = []
    result = ''
    for something in inputs:
        if something in '()+*':
            if something == '(':
                stack.append(something)
            elif something == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(something)
            elif something == '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(something)
            else:
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += something
    while stack:
        result += stack.pop()

    for something in result:
        if something == '*':
            pop1 = int(stack.pop())
            pop2 = int(stack.pop())
            stack.append(pop2*pop1)
        elif something == '+':
            pop1 = int(stack.pop())
            pop2 = int(stack.pop())
            stack.append(pop2 + pop1)
        else:
            stack.append(something)
    print(f'#{test} {stack[0]}')