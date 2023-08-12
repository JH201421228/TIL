import sys
input = sys.stdin.readline

prime_check_list = [True] * 1000001
prime_check_list[0] = False
prime_check_list[1] = False

for i in range(2, int(1000001**0.5) + 1):
    if prime_check_list[i]:
        for j in range(i**2, 1000001, i):
            prime_check_list[j] = False

Test_Case_Num = int(input())

for test_case in range(Test_Case_Num):
    raw_num = int(input())
    check_num = raw_num // 2
    cnt = 0

    for i in range(2, check_num + 1):
        if prime_check_list[i] and prime_check_list[raw_num - i]:
            cnt += 1

    print(cnt)