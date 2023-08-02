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


while True:
    n = int(input())
    
    if n == 0:
        break
        
    else:
        cnt = 0

        for num in range(n + 1, 2*n + 1):
            if prime_checker(num):
                cnt += 1

        print(cnt)