import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    if int(input()) == 1:
        A, B = map(int, input().split())
        
        res = ''
        cur = A+B
        
        for _ in range(13):
            res += chr(cur % 26 + 97)
            cur //= 26
            
        print(res, flush=True)
    
    else:
        cur = input().rstrip()
        
        res = 0
        
        for idx in range(13):
            res += (ord(cur[idx]) - 97) * (26**idx)
    
        print(res)
        
    return


def main():
    
    solve()
    
    return


if __name__ == "__main__":
    main()