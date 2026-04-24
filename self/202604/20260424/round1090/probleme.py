import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    
    ans = 0
    
    for i in range(N-1):
        for j in range(i+1, N):
            ans = max(ans, arr[i] ^ arr[j])
    
    print(ans)
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()