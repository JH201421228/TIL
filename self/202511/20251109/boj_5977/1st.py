import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    def _temp(idx):
        return dp[idx-1] - sums[idx]
    
    N, K = map(int, input().split())
    E = [int(input()) for _ in range(N)]
    sums = [0] * (N+1)
    
    dp = [0] * (N+1)
    
    q = deque([])
    
    for idx in range(1, N+1): sums[idx] = sums[idx-1] + E[idx-1]
    
    for idx in range(1, N+1):
        while (q and q[0] < idx-K): q.popleft()
        while (q and _temp(q[-1]) <= _temp(idx)): q.pop()
        
        q.append(idx)
        
        dp[idx] = sums[idx] + _temp(q[0])
        if (idx <= K): dp[idx] = max(dp[idx], sums[idx])
        
    print(dp[N])
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()