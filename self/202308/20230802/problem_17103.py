import sys
input = sys.stdin.readline

def prime_checker(num):
    if num <= 1:
        return False
    
    else:
        for divide_num in range(2, int(num**0.5) + 1):
            if num % divide_num == 0:
                return False
            
        return True
    

Test_Case = int(input())

for test_case in range(Test_Case):
    test_num = int(input())
    cnt = 0

    for num in range(1, int(test_num/2) + 1, 2):
        if prime_checker(num) and prime_checker(test_num - num):
            cnt += 1

    print(cnt)