import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

ans_list = []
while True:
    input_str = input()
    if input_str == '.':
        break
    inner_list = [i for i in input_str]
    inner_ans_list = []
    for _ in range(len(inner_list)):
        what_input = inner_list.pop()
        if what_input == '(' or what_input == ')' or what_input == '[' or what_input == ']':
            inner_ans_list.append(what_input)
    inner_ans_list.reverse()
    ans_list.append(inner_ans_list)

for inner_list in ans_list:
    small_list = []
    large_list = []
    for char in inner_list:
        if char == '(' or char == ')':
            small_list.append(char)
        else:
            large_list.append(char)
    check_num_1st = 0
    No1 = 0
    for char in small_list:
        if char == ')':
            check_num_1st += 1
        else:
            check_num_1st -= 1

        if check_num_1st == -1:
            No1 = 1
            break


    # print(small_list)
    # print(large_list)