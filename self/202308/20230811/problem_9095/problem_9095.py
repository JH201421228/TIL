import sys
sys.stdin = open('input.txt')


def plus_fucn(n):
    result = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0]

    if n < 4:
        return result[n]
    else:
        for i in range(4, n+1):
            result[i] = result[i-1] + result[i-2] + result[i-3]
        return result[n]


Test_Case = int(input())

for text_case in range(Test_Case):
    n = int(input())
    print(plus_fucn(n))