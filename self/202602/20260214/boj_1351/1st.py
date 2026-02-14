import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def recur(n, p, q, memo):
    if n in memo: return memo[n]
    
    a = recur(n//p, p, q, memo)
    memo[n//p] = a
    b = recur(n//q, p, q, memo)
    memo[n//q] = b
    
    return a+b


def solve():
    N, P, Q = map(int, input().split())
    
    memo = {0: 1}
    
    print(recur(N, P, Q, memo))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()