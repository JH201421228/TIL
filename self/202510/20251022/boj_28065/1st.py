import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    ans = []
    
    for n in range(N):
        ans.append((N - (-1) ** (n+1) * N) // 2 - (-1) ** n * ((n+1)//2))
        
    print(*ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
    