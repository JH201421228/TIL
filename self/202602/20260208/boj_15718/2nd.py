import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 100_007


def lucas(n, k, fac, inv, p):
    res = 1
    
    while n or k:
        a, b = n % p, k % p
        
        if (b > a): return 0
        
        res = res * ((fac[a] * inv[b] % p) * inv[a-b] % p) % p
        
        n //= p
        k //= p
        
    return res


def egcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    
    while b:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return y0


def crt(a, b):
    res = 0
    
    res = (res + (a * 1031 % MOD) * egcd(97, 1031) % MOD) % MOD
    res = (res + (b * 97 % MOD) * egcd(1031, 97) % MOD) % MOD

    return res

def solve(fac1, fac2, inv1, inv2):
    N, M = map(int, input().split())
    
    if not N and M == 1:
        print(1)
        return
    
    if not N:
        print(0)
        return
    
    if M == 1:
        print(0)
        return
    
    a = lucas(N-1, M-2, fac1, inv1, 97)
    b = lucas(N-1, M-2, fac2, inv2, 1031)
    
    print(crt(a, b))
    
    return


def main():
    fac1 = [1] * 97
    fac2 = [1] * 1031
    inv1 = [0] * 97
    inv2 = [0] * 1031
    
    for i in range(1, 97): fac1[i] = fac1[i-1] * i % 97
    for i in range(1, 1031): fac2[i] = fac2[i-1] * i % 1031
    
    inv1[96] = egcd(97, fac1[96])
    inv2[1030] = egcd(1031, fac2[1030])
    
    for i in range(96, 0, -1): inv1[i-1] = inv1[i] * i % 97
    for i in range(1030, 0, -1): inv2[i-1] = inv2[i] * i % 1031
    
    for _ in range(int(input())): solve(fac1, fac2, inv1, inv2)
    
    return


if __name__ == "__main__":
    main()