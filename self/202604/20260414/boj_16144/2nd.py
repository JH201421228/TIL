import sys
from fractions import Fraction
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    
    lower = Fraction(0, 1)
    upper = Fraction(256, 1)
    
    for i in range(N):
        for j in range(i+1, N):
            d = j-i
            
            lo = Fraction(nums[j] - nums[i] - 1, d)
            hi = Fraction(nums[j] - nums[i] + 1, d)
            
            if lo > lower:
                lower = lo
                
            if upper > hi:
                upper = hi
            
    if lower < upper:
        print("pass")
    else:
        print("fail")
        
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()