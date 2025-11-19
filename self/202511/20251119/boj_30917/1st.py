import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    q = 0
    ans = 0
    
    while True:
        q += 1
        print("? A", q, flush=True)
        res = int(input())
        
        if res:
            ans += q
            break
        
    q = 0
    while True:
        q += 1
        print("? B", q, flush=True)
        res = int(input())
        
        if res:
            ans += q
            break
        
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()