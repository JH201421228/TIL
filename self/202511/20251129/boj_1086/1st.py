import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a%b
    
    return a


def solve():
    N = int(input())
    seq = [int(input()) for _ in range(N)]
    K = int(input())
    
    dp = [[0] * (K) for _ in range(1<<N)]
    dp[0][0] = 1
    
    next_seq = [[(j * (10**(len(str(seq[i])))) + seq[i]) % K for j in range(K)]  for i in range(N)]
    
    for cur in range(1<<N):
        for i in range(N):
            if cur&(1<<i): continue
            
            for j in range(K):
                dp[cur|(1<<i)][next_seq[i][j]] += dp[cur][j]

    a, b = dp[-1][0], sum(dp[-1])
    c = gcd(b, a)
    
    print(f"{a//c}/{b//c}")

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()