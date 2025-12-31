import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    string = input().rstrip()
    N = len(string)
    
    is_pal = {i: [] for i in range(N)}
    
    for idx in range(N):
        
        i = 0
        while True:
            if idx-i < 0: break
            if idx+i >= N: break
            
            if string[idx+i] != string[idx-i]: break
            is_pal[idx+i].append(2*i+1)
            
            i += 1
            
        if idx == 0: continue
        
        i = 0
        while True:
            if idx-1-i < 0: break
            if idx+i >= N: break
            
            if string[idx+i] != string[idx-1-i]: break
            is_pal[idx+i].append(2*i+2)
            
            i += 1
            
    dp = [float("inf")] * (N+1)
    dp[0] = 0
    
    for idx in range(N):
        for v in is_pal[idx]:
            if idx+1-v >= 0: dp[idx+1] = min(dp[idx+1], dp[idx+1-v]+1)
            
    print(dp[-1])
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()