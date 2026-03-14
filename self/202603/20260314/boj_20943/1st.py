import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
        
    return a


def solve():
    N = int(input())
    
    candidates = {}
    
    for _ in range(N):
        a, b, c = map(int, input().split())
        if a == 0: candidates[(0, 1)] = candidates.get((0, 1), 0) + 1
        elif b == 0: candidates[(1, 0)] = candidates.get((1, 0), 0) + 1
        else:
            if a*b > 0:
                a, b = abs(a), abs(b)
                a, b = max(a, b), min(a, b)
                d = gcd(a, b)
                candidates[(a//d, b//d)] = candidates.get((a//d, b//d), 0) + 1
                
            else:
                a, b = abs(a), abs(b)
                a, b = max(a, b), min(a, b)
                d = gcd(a, b)
                candidates[(a//d, -b//d)] = candidates.get((a//d, -b//d), 0) + 1
    
    ans = 0
    for v in candidates.values():
        ans += v * (N-v)
    
    print(ans // 2)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()