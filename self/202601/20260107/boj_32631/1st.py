import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    
    
    
    for idx in range(1, N+1):
        A[idx] += A[idx-1]
        B[idx] += B[idx-1]
    
    ans = max(A[-1], B[-1])
    
    for i in range(K+1):
        min_A, min_B = A[-1], B[-1]
        
        for idx in range(i+1):
            min_A = min(min_A, A[N-i+idx] - A[idx])
        for idx in range(K-i+1):
            min_B = min(min_B, B[N-K+i+idx] - B[idx])
            
        ans = min(ans, max(min_A, min_B))
        
        
    print(ans)
            
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()