import sys
sys.stdin = open('input.txt')

Test = int(input())

for test in range(Test):
    str_size = int(input())
    input_str = input()
    input_int = []
    for char in input_str:
        input_int.append(int(char))

    input_int.sort()
    ans_dict = {}
    for val in input_int:
        ans_dict[val] = ans_dict.get(val, 0) + 1
    ans_val = 0
    ans_num = 0
    for val, num in ans_dict.items():
        if num >= ans_num:
            ans_val = val
            ans_num = num

    print(f'#{test+1} {ans_val} {ans_num}')