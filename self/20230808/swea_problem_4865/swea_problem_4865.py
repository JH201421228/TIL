import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    str1 = list(input())
    str2 = list(input())
    str_dict = {}

    for char in str2:
        str_dict[char] = str_dict.get(char, 0) + 1

    max_val = 0

    for char in str1:
        if str_dict[char] > max_val:
            max_val = str_dict[char]

    print(f'#{test_case + 1} {max_val}')