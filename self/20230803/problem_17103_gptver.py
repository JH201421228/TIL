import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 에라토스테네스의 체를 사용하여 소수 판별 리스트를 미리 생성
N = 1000001
prime_check_list = [False] * N
prime_check_list[0] = True
prime_check_list[1] = True

for i in range(2, int(N**0.5) + 1):
    if not prime_check_list[i]:
        for j in range(i*i, N, i):
            prime_check_list[j] = True

Test_Case = int(input())
for test_case in range(Test_Case):
    test_num = int(input())
    real_num = test_num//2
    cnt = 0

    for num in range(2, real_num + 1):
        if not prime_check_list[num] and not prime_check_list[test_num - num]:
            cnt += 1

    print(cnt)
