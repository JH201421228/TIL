import sys
input = sys.stdin.readline

Test_case = int(input())

for test_case in range(Test_case):
    A, B = map(int, input().split())

    # for num in range(max(A, B), A*B+1):
    # for num in range(A*B, max(A, B)-1, -1):
    #     if num % A == 0 and num % B == 0:
    #         print(num)
    max_val = max(A, B)
    min_val = min(A, B)

    for num in range(1, min_val+1):
        if (max_val*num) % min_val == 0:
            print(max_val*num)
            break