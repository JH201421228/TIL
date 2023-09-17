import sys
sys.stdin = open('input.txt')

equation = list(input().split('-'))
# print(equation)
ans_list = []
for inner in equation:
    inner_list = list(inner.split('+'))
    temp = 0
    for str_num in inner_list:
        temp += int(str_num)
    ans_list.append(temp)
print(ans_list[0] * 2 - sum(ans_list))
