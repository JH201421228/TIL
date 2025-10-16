import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    
    if N == K:
        print("Impossible")
        return
    
    ans = []
    
    for n in range(2, 2+N-K-1):
        ans.append(n)
        
    ans.append(1)
    
    for n in range(2+N-K-1, N+1):
        ans.append(n)
        
    print(*ans)
    
    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()