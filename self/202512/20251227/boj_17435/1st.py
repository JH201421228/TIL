import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    M = int(input())
    
    dp = [[0] * (M+1) for _ in range(19)]
    
    temp = list(map(int, input().split()))
    for idx in range(M): dp[0][idx+1] = temp[idx]
    
    for i in range(1, 19):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][dp[i-1][j]]
          
    output = ""
            
    for _ in range(int(input())):
        a, b = map(int, input().split())
        
        ans = b
        
        for i in range(19):
            if a & (1<<i): ans = dp[i][ans]
            
        output += str(ans) + '\n'
    
    print(output)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()