import sys
import heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    has = [list(map(int, input().split())) for _ in range(n)]
    shop = [list(map(int, input().split())) for _ in range(m)]
    
    pq = []
    
    for x, y in has: heapq.heappush(pq, [y, -x])
    
    while pq:
        print(heapq.heappop(pq))
        
    print("-" * 50)
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()