import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def nCr(n, r, fac):
    return fac[n] // fac[r] // fac[n-r]


def solve():
    N = int(input())
    P, Q = map(float, input().split())
    
    fac = [1] * (N+1)
    for i in range(1, N+1): fac[i] = fac[i-1]*i
    
    ans = 0
    possible = [pow(Q, i) * pow(1-Q, N-i) * nCr(N, i, fac) for i in range(N+1)]
    
    for i in range(N+1):
        temp = [pow(P, ii) * pow(1-P, i-ii) * nCr(i, ii, fac) for ii in range(i+1)]
        tmp = 0
        for idx in range(len(possible)):
            for jdx in range(len(temp)):
                if idx+jdx < N+1: tmp += (idx+jdx) * possible[idx] * temp[jdx]
                
        ans = max(ans, tmp)
                    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()