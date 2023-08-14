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
    large_bracket_checker = 0
    small_bracket_checker = 0
    for char in inner_list:
        if char == ')':
            small_bracket_checker -= 1
        elif char == '(':
            small_bracket_checker += 1
        elif char == ']':
            large_bracket_checker -= 1
        elif char == '[':
            large_bracket_checker += 1

        if small_bracket_checker < 0 or large_bracket_checker < 0:
            break

    if small_bracket_checker == 0 and large_bracket_checker == 0:
        print('yes')
    else:
        print('no')