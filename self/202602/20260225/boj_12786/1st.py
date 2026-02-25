import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    T = int(input())
    
    tree = [list(map(int, input().split()))[1:] for _ in range(N)]

    ans = float("inf")
    
    V = [[[0] * (T+1) for _ in range(21)] for _ in range(N+1)]
    
    q = deque([(1, 0, 0)])

    while q:
        h, n, t = q.popleft()
        
        if n == N:
            ans = min(ans, t)
            continue
        
        available = tree[n]
        
        cand = [h, h+1, h-1, min(h*2, 20)]
        flag = 0
        for c in set(cand):
            if  c in available and not V[n+1][c][t]:
                V[n+1][c][t] = 1
                flag = 1
                q.append((c, n+1, t))
                
        if not flag and t < T:
            for a in available:
                if not V[n+1][a][t+1]:
                    V[n+1][a][t+1] = 1
                    q.append((a, n+1, t+1))
              
    if ans == float("inf"): print(-1)
    else: print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()