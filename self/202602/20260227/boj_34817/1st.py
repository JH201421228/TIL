import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    max_v = arr[0]
    
    for idx in range(1, N):
        cur = arr[idx]
        
        if max_v - K > cur:
            print("NO")
            return
        
        max_v = max(max_v, cur)
    
    print("YES")
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()