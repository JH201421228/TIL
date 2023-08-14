import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):

    short_str = list(input())
    large_str = list(input())
    i = 0
    N = len(short_str)
    ans = 0
    for char in large_str:
        if char == short_str[i]:
            i += 1
        else:
            i = 0

        if i == N:
            ans = 1
            break

    if ans == 1:
        print(f'#{test_case + 1} 1')
    else:
        print(f'#{test_case + 1} 0')