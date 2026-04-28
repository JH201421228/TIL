import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    
    target_n = max(arr)
    
    ans = 0
    
    for a in arr:
        if a == target_n: ans += 1
        
    print(ans)
        
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()