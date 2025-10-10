import sys
import heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    hq = list(map(int, input().split()))
    
    heapq.heapify(hq)
    
    for _ in range(N-1):
        for x in input().split():
            heapq.heappush(hq, int(x))

        for _ in range(N):
            heapq.heappop(hq)
            
    print(heapq.heappop(hq))
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()