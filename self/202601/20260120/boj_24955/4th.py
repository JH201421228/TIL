import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 1_000_000_007


def bfs(x, y, N, G, A):
    q = deque([x])
    V = [0] * (N+1)
    V[x] = 1
    ans = [0] * (N+1)
    ans[x] = A[x-1]
    
    while q:
        n = q.popleft()
        for x in G[n]:
            if not V[x]:
                V[x] = 1
                ans[x] = int(str(ans[n]) + str(A[x-1])) % MOD
                q.append(x)
    
    return ans[y]


def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    G = [[] for _ in range(N+1)]
    
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
        
    for _ in range(Q):
        x, y = map(int, input().split())
        print(bfs(x, y, N, G, A))
        
    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()