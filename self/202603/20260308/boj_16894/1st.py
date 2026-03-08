import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def sieve(n):
    res = [1] * (int(n**.5)+1)
    res[1] = 0
    
    for i in range(1, int(n**.5)+1):
        if res[i]:
            for j in range(i**2, int(n**.5)+1, i): res[j] = 0
    
    return res


def solve():
    n = int(input())
    
    if n == 1:
        print("koosaga")
        return
    
    is_prime = sieve(n)
    
    cnt = 0
    
    for i in range(2, int(n**.5)+1):
        if is_prime[i]:
            while n % i == 0:
                cnt += 1
                n //= i
                
                if cnt > 2:
                    print("koosaga")
                    return
                
    if n != 1: cnt += 1
    
    if cnt == 2:
        print("cubelover")
    else:
        print("koosaga")
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()