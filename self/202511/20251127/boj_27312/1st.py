import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    M, N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    ans = []
    
    for idx in range(M):
        print(f"? {idx+1} {idx+1}", flush=True)
        
        if int(input()) < A[idx]: ans.append(A[idx])
        else: ans.append(A[idx]-1)
        
    for _ in range(N-M):
        ans.append(1)
        
    print("!", *ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()