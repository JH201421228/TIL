import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 998_244_353


def solve():
    # (1~X 까지 합) ^ 2 * (X)^(K-1) * (X)^(N-1)
    
    N, K, X = map(int, input().split())
    
    n = 1
    for i in range(2, X+1): n = (n+i) % MOD
    n = (n*n) % MOD
    
    total = N+K-2
    res = X
    tmp = 1
    while total:
        if total & 1:
            tmp = (tmp*res) % MOD
        res *= res
        res %= MOD
        total >>= 1
        
    n = (n*tmp) % MOD
    
    ans = [n*K%MOD] * (N-K+1)
    
    print(*ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()