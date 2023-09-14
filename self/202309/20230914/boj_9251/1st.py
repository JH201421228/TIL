import sys
sys.stdin = open('input.txt')

first_list = list(input())
second_list = list(input())
# print(first_list, second_list)
length1 = len(first_list)+1
length2 = len(second_list)+1
check_list = [[0] * length2 for _ in range(length1)]
for i in range(1, length1):
    for j in range(1, length2):
        if first_list[i-1] == second_list[j-1]:
            check_list[i][j] = check_list[i-1][j-1] + 1
        else:
            check_list[i][j] = max(check_list[i][j-1], check_list[i-1][j])
print(check_list[-1][-1])