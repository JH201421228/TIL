import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    q, p = [], []
    
    for _ in range(N):
        a, b = map(int, input().split())
        
        if a < b: q.append((a, b))
        else: p.append((-b, -a))
        
    heapq.heapify(q)
    heapq.heapify(p)
    
    virtual, ans = 0, 0
    
    while q:
        n, x = heapq.heappop(q)
        
        if virtual + ans < n: ans = n - virtual
        
        virtual += (x - n)
        
    while p:
        x, n = heapq.heappop(p)

        if -n > ans + virtual: ans = -n - virtual
        
        virtual -= x
        virtual += n
        
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()