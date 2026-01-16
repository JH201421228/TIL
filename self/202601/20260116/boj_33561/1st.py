import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())
    D = list(map(int, input().split()))
    
    zeros = [[0] * (N+1) for _ in range(N+1)]
    area = [[0] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            cur = W[i-1][j-1]
            area[i][j] = area[i-1][j] + area[i][j-1] - area[i-1][j-1] + cur
            zeros[i][j] = zeros[i-1][j] + zeros[i][j-1] - zeros[i-1][j-1]
            if not cur: zeros[i][j] += 1
            
    D.sort(reverse=True)
    for idx in range(1, K): D[idx] += D[idx-1]
    
    ans = 0
    
    for k in range(1, N+1):
        for i in range(k, N+1):
            for j in range(k, N+1):
                cur_zeros = zeros[i][j] - zeros[i-k][j] - zeros[i][j-k] + zeros[i-k][j-k]
                if cur_zeros > K: continue
                
                cur_area = area[i][j] - area[i-k][j] - area[i][j-k] + area[i-k][j-k]
                if cur_zeros: cur_area += D[cur_zeros-1]
                
                ans = max(ans, cur_area)
            
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()