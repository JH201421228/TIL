alpha = 'abcdefghijklmnopqrstuvwxyz'
check_list = [-1]*len(alpha)
input_str = input()

# input_list = []
# for i in input_str:
#     input_list.append(i)

for i in alpha:
    if i in input_str:
        check_list[i] = input_str.index(i)

print(check_list)