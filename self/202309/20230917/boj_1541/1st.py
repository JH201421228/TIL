import sys
sys.stdin = open('input.txt')


thing = input()
input_list = []
number = ''
for some in thing:
    if some in '+-':
        input_list.append(int(number))
        number = ''
        input_list.append(some)
    else:
        number += some
input_list.append(int(number))
# print(input_list)

ans = 0
temp = 0
for x in input_list:

    if x == '-':
        ans == temp
        temp = 0
    elif x == '+':
        pass
    else:
        temp += x
ans -= temp
print(ans)
