import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    status = [input().rstrip() for _ in range(2)]
    
    status = [(10 + int(status[1][i]) - int(status[0][i])) % 10 for i in range(N)]
    
    dp = [[float("inf")] * 10 for _ in range(N)]
    
    for i in range(10):
        if i == status[0]:
            dp[0][i] = i
        else:
            dp[0][i] = i + 10 - (status[0]+10-i) % 10
        
            
    for i in range(1, N):
        for j in range(10):
            for k in range(10):

                if j == status[i]:
                    delta = (j-k+10) % 10
                else:
                    delta = (j-k+10) % 10 + 10 - (status[i]+20-j) % 10 
                
                dp[i][j] = min(dp[i][j], dp[i-1][k] + delta)

    print(min(dp[-1]))
                
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()