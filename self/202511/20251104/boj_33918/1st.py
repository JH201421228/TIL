import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, M, C, D = map(int, input().split())
    B = list(map(int, input().split()))
    
    dp = [[0] * (M+1) for _ in range(N)]
    
    for time in range(N):
        for temp in range(1, M+1):
            dp[time][temp] = M-abs(temp-B[time])
    
    for time in range(N-1):
        
        for offset in range(1, C+1):
            pq = []
            
            for temp in range(offset, min(offset+D, M)+1, C):
                heapq.heappush(pq, (-dp[time][temp], temp))
                
            for temp in range(offset, M+1, C):
                if temp != offset and temp+D < M+1: heapq.heappush(pq, (-dp[time][temp+D], temp+D))
                
                while pq and pq[0][1] + D < temp: heapq.heappop(pq)
                
                dp[time+1][temp] -= pq[0][0]
                
    print(max(dp[-1]))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()