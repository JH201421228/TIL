import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    string = input().rstrip()
    
    cnt = 0
    length = len(string)
    for idx in range(1, length):
        MOD = string[length-idx:length]
        
        if len(str(int(MOD))) != len(MOD) or int(MOD) == 0: continue
        
        MOD = int(MOD)
        
        # if string[0] == "0": continue
        
        dp = [0] * (length-idx)
        
        for i in range(1, length-idx+1):
            
            if len(str(int(string[:i]))) != len(string[:i]): continue
            
            if int(string[:i]) < MOD: dp[i-1] += 1

            if i == length-idx:
                cnt += dp[-1]
                continue
            
            for j in range(1, i+1):
                if len(str(int(string[i-j+1:i+1]))) == len(string[i-j+1:i+1]) and int(string[i-j+1:i+1]) < MOD:
                    dp[i] += dp[i-j]
                
    print(cnt)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()