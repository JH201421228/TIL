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
    input_num = int(input().rstrip())

    while True:
        if prime_checker(input_num):
            break
    
        input_num += 1
    
    print(input_num)

