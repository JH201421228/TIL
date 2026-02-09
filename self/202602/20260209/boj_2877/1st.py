import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    K = int(input())
    K -= 1
    
    n = 0
    
    while K >= 0:
        n += 1
        K -= 2**n
        
    
    ans = 0
    for i in range(n):
        if K % 2: ans += 7*(10**i)
        else: ans += 4*(10**i)
        
        K //= 2
        
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()