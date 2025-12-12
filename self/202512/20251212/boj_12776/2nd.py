import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    q, r, maxv, minv = [], 0, 0, float("inf")
    
    for _ in range(N):
        a, b = map(int, input().split())
        
        if a < b: q.append((a, b))
        else:
            r += a-b
            maxv = max(maxv, a)
            minv = min(minv, b)
        
    heapq.heapify(q)
    
    virtual, ans = 0, 0
    
    while q:
        n, x = heapq.heappop(q)
        
        if virtual + ans < n: ans = n - virtual
        
        virtual += (x - n)
        
    
    if ans + virtual >= max(maxv, r): print(ans)
    else: print(r+minv-virtual)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()