import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    
    arr = []
    for _ in range(N):
        arr.append(tuple(map(int, input().split())))
        
    arr.sort(key=lambda x : x[1], reverse=True)
    
    cur_d = K
    idx = 0
    pq = []
    
    cur_s, cur_c, cur_t = 0, 0, 0
    
    ans = 0
    
    while cur_d > 0:
        while idx < N and arr[idx][1] >= cur_d:
            c, t, s = arr[idx]
            idx += 1
            heapq.heappush(pq, (-s, c, t))
        
        if idx < N: nxt_d = arr[idx][1]
        else: nxt_d = 0
        
        gap = cur_d - nxt_d
        
        while gap > 0 and pq:
            s, c, t = heapq.heappop(pq)
            s *= -1
            
            amount = min(gap, c)
            
            ans += amount * s
            gap -= amount
            c -= amount
            
            if c > 0: heapq.heappush(pq, (-s, c, t))
            
        cur_d = nxt_d
    

    return ans


def main():
    for i in range(int(input())):
        print(f"Case #{i+1}: {solve()}")
    
    return


if __name__ == "__main__":
    main()