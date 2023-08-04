# 초심자의 회문 검사
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())
def palindrome(input_str):
    length_str = len(input_str)
    for index in range(int(length_str/2) + 1):
        if input_str[index] != input_str[-1 - index]:
            return 0
    return 1
for test_case in range(Test_Case):
    check_str = input()
    print(f'#{test_case + 1} {palindrome(check_str)}')