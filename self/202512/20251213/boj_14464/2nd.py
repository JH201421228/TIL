import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    C, N = map(int, input().split())
    ck = [int(input()) for _ in range(C)]
    cow = [tuple(map(int, input().split())) for _ in range(N)]
    ck.sort()
    cow.sort()
    
    pq = []
    cow_idx = 0
    
    ans = 0
    
    for c in ck:
        while True:
            if cow_idx >= N: break
            elif cow[cow_idx][0] <= c:
                heapq.heappush(pq, cow[cow_idx][1])
                cow_idx += 1
            else: break
            
        while pq and pq[0] < c: heapq.heappop(pq)
        
        if pq:
            heapq.heappop(pq)
            ans += 1
    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()