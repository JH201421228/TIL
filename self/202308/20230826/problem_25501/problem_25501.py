import sys
sys.stdin = open('input.txt')


def palindrome_checker(start, end):
    if start >= end:
        print(1, start + 1)
        return [1, start]

    elif string[start] != string[end]:
        print(0, start + 1)
        return [0, start]

    else:
        palindrome_checker(start+1, end-1)


n = int(input())
for _ in range(n):
    string = input()
    palindrome_checker(0, len(string)-1)