import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    L, N = map(int, input().split())
    S = input().rstrip()
    
    box = ["w", "h"]
    splited = []
    s, e = 0, 0
    flag = 0
    while True:
        if e > L-1: break
        if flag and S[e] not in box:
            flag = 0
            splited.append(S[s:e])
            s = e
        elif not flag and S[e] in box:
            flag = 1
            splited.append(S[s:e])
            s = e
        e += 1
        
    splited.append(S[s:e])
    
    ans = []
    
    l = 1
    if splited[0]: l = 0
    
    for spl in splited[l:]:
        if spl[0] not in box:
            ans.append(spl)
            continue
        
        temp = ["w"] * len(spl)
        cur = 0
        for idx in range(len(spl)):
            if spl[idx] == "h":
                cur = max(cur, idx-N)
                temp[cur] = "h"
                cur += 1
                
        ans.append("".join(temp))
            
    print("".join(ans))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()