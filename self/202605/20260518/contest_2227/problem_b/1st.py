import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    S = input().rstrip()
    
    ans = 0
    
    for s in S:
        if s == '(': ans += 1
        else: ans -= 1
        
    if ans: print("NO")
    else: print("YES")
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()