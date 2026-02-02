import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 1_000_000_007
mods = [1] * 4_000_001


def recur(cur, n):
    
    if not n: return 1
    
    if n%2:
        n -= 1
        return (((recur(cur, n//2) ** 2) % MOD) * cur) % MOD
    else:
        return (recur(cur, n//2) ** 2) % MOD


def solve():
    N, K = map(int, input().split())
    
    print(((mods[N] * recur(mods[K], MOD-2)) % MOD) * recur(mods[N-K], MOD-2) % MOD)
    
    return


def main():
    
    for i in range(2, 4_000_001):
        mods[i] = (mods[i-1] * i) % MOD
    
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()