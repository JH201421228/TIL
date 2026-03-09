import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 1_000_000_007


def solve():
    N, M, A = map(int, input().split())
    H = int(input())
    
    print(pow(M, N-1, MOD))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()