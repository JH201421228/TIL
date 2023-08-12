import sys
sys.stdin = open('input.txt')

num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

Test_Case = int(input())

for test_case in range(Test_Case):
    input_list = list(map(str, input().split()))
    odd_nums = list(map(str, input().split()))
    counts = [0] * 10
    for char in odd_nums:
        counts[num_list.index(char)] += 1

    print(f'#{test_case + 1}')
    for i in range(10):
        print((num_list[i] + ' ') * counts[i], end='')

    print()
