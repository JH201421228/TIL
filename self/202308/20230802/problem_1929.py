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

start_num, end_num = map(int, input().split())

for num in range(start_num, end_num + 1):
    if prime_checker(num):
        print(num)