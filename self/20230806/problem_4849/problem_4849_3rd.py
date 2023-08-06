import sys
sys.stdin = open('input.txt')

input_list = []
while True:
    input_str = input()
    if input_str == '.':
        break
    censored_inner_list = []
    for char in input_str:
        if char == '(' or char == ')' or char == '[' or char == ']':
            censored_inner_list.append(char)

    input_list.append(censored_inner_list)

for inner_list in input_list:
    ans_stack = []
    while inner_list:
        move_char = inner_list.pop()
        if ans_stack:
            if (move_char == '(' and ans_stack[-1] == ')') or (move_char == '[' and ans_stack[-1] == ']'):
                del ans_stack[-1]
            else:
                ans_stack.append(move_char)
        else:
            ans_stack.append(move_char)

    if ans_stack:
        print('no')
    else:
        print('yes')