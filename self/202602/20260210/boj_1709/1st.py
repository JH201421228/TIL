import sys
from math import isqrt
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    N //= 2
    prev = N-1
    cnt = 1
    
    if N == 1:
        print(4)
        return
    
    for x in range(1, N+1):
        t = N**2 - x**2
        cur = isqrt(t)
        
        if cur < x: break
        
        cnt += 1 + prev - cur
        prev = cur
        
        if cur**2 == t: cnt -= 1
        
    print(cnt * 8 + 4)

    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()