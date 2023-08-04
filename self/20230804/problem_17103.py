N = 1000001
prime_check_list = [True] * N
prime_check_list[0] = [False]
prime_check_list[1] = [False]

for i in range(2, N):
    if prime_check_list[i]:
        for j in range(i*i, N, i):
            prime_check_list[j] = False

Test_Case = int(input())

for test_case in range(Test_Case):
    check_num = int(input())
    half_num = check_num // 2
    cnt = 0
    for num in range(2, half_num+1):
        if prime_check_list[num] and prime_check_list[check_num - num]:
            cnt += 1

    print(cnt)