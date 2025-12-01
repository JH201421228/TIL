import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    
    if N%2:
        resp = list(map(int, input().split()))
        cur = 0
        
        for i in resp:
            cur |= (1<<(i-1))
            
        ans = []
        
        for i in range(1, N+1):
            if cur & (1<<(i-1)): continue
            ans.append(i)
            
        print(N, len(ans), flush=True)
        print(*ans, flush=True)
        
    else:
        resp = list(map(int, input().split()))
        cur = 0
        
        for i in resp:
            cur |= (1<<(i-1))
            
        ans = []
        
        if cur == (1<<N):
            print(N, 0, flush=True)
            print(flush=True)
            return
        
        if cur & 1: ans.append(1)
        
        for i in range(2, N+1):
            if cur & (1<<(i-1)): continue
            ans.append(i)
            
        print(N, len(ans), flush=True)
        print(*ans, flush=True)
    
    
    return


def main():
    for _ in range(int(input())):
        solve()
    
    return


if __name__ == "__main__":
    main()