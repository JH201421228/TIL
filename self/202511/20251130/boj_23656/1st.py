import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    s, e = 1, 1_000_000_000
    
    while True:
        mid = (s+e) >> 1
        
        cur = int(input())
        
        if cur < s:
            print(">", flush=True)
            continue
        
        if cur > e:
            print("<", flush=True)
            continue
            
        if s >= e and (s == cur or e == cur):
            print("=", flush=True)
            break
        
        if cur > mid:
            print("<", flush=True)
            e = cur-1
        else:
            print(">", flush=True)
            s = cur+1
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()