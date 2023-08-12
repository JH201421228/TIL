import sys
input = sys.stdin.readline
#2 < N <= 1000000

prime_check_list = [0] * 1000001
prime_check_list[0] = 1
prime_check_list[1] = 1
while True:
    prime_num_now = prime_check_list.index(0)
    prime_check_list[prime_num_now] = -1
    if prime_num_now > 1000:
        break
    i = 2
    while True:
        prime_check_list[prime_num_now*i] = 1
        i += 1
        if i*prime_num_now > 1000000:
            break

Test_Case = int(input())
for test_case in range(Test_Case):
    test_num = int(input())
    real_num = test_num//2
    cnt = 0

    for num in range(3, real_num+1):
        if prime_check_list[num] == -1 and prime_check_list[test_num - num] == -1:
            cnt += 1

    print(f'ans = {cnt}')