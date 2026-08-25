import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    
    n_dict = dict()
    
    zeros = []
    for idx in range(2*N):
        if not arr[idx]: zeros.append(idx)
        
    mid = zeros[0]
    l, r = mid-1, mid+1
    V = [0] * (N+1)
    V[0] = 1
    while l >= 0 and r < 2*N:
        if arr[l] == arr[r]:
            V[arr[l]] = 1
            l -= 1
            r += 1
            
    mid = zeros[1]
    l, r = mid-1, mid+1
    while l >= 0 and r < 2*N:
        if arr[l] == arr[r]:
            V[arr[l]] = 1
            l -= 1
            r += 1
            
    
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()