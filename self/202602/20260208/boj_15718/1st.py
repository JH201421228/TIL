import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 100_007


def binary_exponentiation(n):
    res = 1
    p = MOD-2
    
    while p:
        if p%2:
            res = res * n % MOD
            
        n *= n
        n %= MOD
        p //= 2
    
    return res


def solve(mods):
    N, M = map(int, input().split())
    
    a = pow(mods[MOD], (N-1)//MOD, MOD)
    a = a * mods[(N-1)%MOD] % MOD
    
    b = pow(mods[MOD], (M-2)//MOD, MOD)
    b = b * mods[(M-2)%MOD] % MOD
    
    c = pow(mods[MOD], (N-M+1)//MOD, MOD)
    c = c * mods[(N-M+1)%MOD] % MOD
    
    
    print(a * binary_exponentiation(b * c % MOD) % MOD)
    
    return


def main():
    mods = [1] * (MOD+1)
    for i in range(2, MOD+1): mods[i] = mods[i-1] * i % MOD
    
    for _ in range(int(input())): solve(mods)
    
    return



if __name__ == "__main__":
    main()