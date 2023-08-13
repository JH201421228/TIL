import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    word = input()
    stack1 = []
    stack2 = []
    for char in word:
        if char == '(' or char == ')' or char == '{' or char == '}' :
            stack1.append(char)
    while stack1:
        if stack1[-1] == '(' and stack2 and stack2[-1] == ')':
            stack1.pop()
            stack2.pop()
        elif stack1[-1] == '{' and stack2 and stack2[-1] == '}':
            stack1.pop()
            stack2.pop()
        else: stack2.append(stack1.pop())

    if stack2:
        print(f'#{test_case+1} 0')
    else:
        print(f'#{test_case+1} 1')