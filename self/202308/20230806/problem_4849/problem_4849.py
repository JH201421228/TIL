import sys
sys.stdin = open('input.txt')

input_list = []
while True:
    input_str = input()
    if input_str == '.':
        break
    censored_small_list = []
    censored_large_list = []
    for char in input_str:
        if char == '(' or char == ')':
            censored_small_list.append(char)
        elif char == '[' or char == ']':
            censored_large_list.append(char)
    input_list.append([censored_small_list, censored_large_list])

for inner_list in input_list:
    small_bracket_num = 0
    large_bracket_num = 0
    small_bracket_checker = False
    large_bracket_checker = False
    for small_bracket in inner_list[0]:
        if small_bracket == ')':
            small_bracket_num += 1
        else:
            small_bracket_num -= 1

        if small_bracket_num < 0:
            break

    if small_bracket_num == 0:
        small_bracket_checker = True

    for large_bracket in inner_list[1]:
        if large_bracket == ']':
            large_bracket_num += 1
        else:
            large_bracket_num -= 1

        if large_bracket_num < 0:
            break

    if large_bracket_num == 0:
        large_bracket_checker = True

    if small_bracket_checker and large_bracket_checker:
        print('yes')
    else:
        print('no')