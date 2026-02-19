import sys, datetime
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    times = [tuple(map(int, input().split())) for _ in range(2)]
    
    diff = datetime.datetime(*times[1]) - datetime.datetime(*times[0])
    
    T, N = map(int, input().split())
    
    dp = [[0] * (T+1) for _ in range(N+1)]
    
    methods = []
    for _ in range(N):
        x, a, b = map(int, input().split())
        if x == 3: b *= 30
        methods.append((a, b))
    
    for i in range(1, N+1):
        a, b = methods[i-1]
        for j in range(1, T+1):
            if j >= a: dp[i][j] = max(dp[i-1][j-a]+b, dp[i-1][j])
            else: dp[i][j] = dp[i-1][j]
            
    print(abs(diff.days - dp[-1][-1]))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()