import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    s = input().rstrip()
    
    s = s.split("100")
    
    if s[0] == '': s = s[1:]
    else:
        if ''.join(s[0].split("01")): return False
        else: s = s[1:]
    
    for ss in s:
        if not ss: return False
        if ss == '1': continue
        
        l = len(ss)
        idx = 0
        flag = False
        
        while idx < l:
            if not flag:
                if ss[idx] == '0':
                    idx += 1
                else:
                    flag = not flag
                    idx += 1
            else:
                if ss[idx] == '1':
                    idx += 1
                else:
                    break
                
        if not flag: return False
        
        temp = ss[idx:]
        temp = temp.split("01")
        
        for t in temp:
            if t: return False
            
    
    return True


def main():
    for _ in range(int(input())):
        if solve(): print("YES")
        else: print("NO")
    
    return


if __name__ == "__main__":
    main()