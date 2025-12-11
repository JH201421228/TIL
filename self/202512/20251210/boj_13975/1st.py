import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    pq = list(map(int, input().split()))
    heapq.heapify(pq)
    
    ans = 0
    while (len(pq) > 1):
        cur = 0
        for _ in range(2):
            cur += heapq.heappop(pq)
            
        ans += cur
        heapq.heappush(pq, cur)
        
    print(ans)
    
    return


def main():
    for _ in range(int(input())):
        solve()
    
    return


if __name__ == "__main__":
    main()