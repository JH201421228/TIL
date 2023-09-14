import sys
sys.stdin = open('input.txt')

first_list = list(input())
second_list = list(input())
print(first_list, second_list)
check_list = [1] * len(first_list)
