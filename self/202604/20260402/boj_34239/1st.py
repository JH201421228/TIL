import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    A = [0] + A
    B = [*A]
    B[1] *= -1
    
    for idx in range(2, N+1):
        A[idx] = A[idx-1] + A[idx] * ((-1)**(idx+1))
        B[idx] = B[idx-1] + B[idx] * ((-1)**(idx))
    
    A_idx = [0] * (N+1)
    B_idx = [0] * (N+1)
    A_idx[-1] = N
    B_idx[-1] = N
    
    for idx in range(N-1, -1, -1):
        if A[idx] > A[A_idx[idx+1]]: A_idx[idx] = idx
        else: A_idx[idx] = A_idx[idx+1]
        
        if B[idx] > B[B_idx[idx+1]]: B_idx[idx] = idx
        else: B_idx[idx] = B_idx[idx+1]
    
    ans = -float("inf")
    
    for l in range(N):
        if l % 2:
            ans = max(B[B_idx[l+1]] - B[l], ans)
        else:
            ans = max(A[A_idx[l+1]] - A[l], ans)
            
    print(ans)

    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()