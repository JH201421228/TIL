import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs(V, G):
    q = deque([1])
    
    V[1] = 0
    
    while q:
        n = q.popleft()
        
        if not G[n]:
            return "yes"
        
        for x in G[n]:
            if not V[x]:
                V[x] = 1
                q.append(x)
                
    return "Yes"


def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        
    S = int(input())
    
    Ss = list(map(int, input().split()))
    
    V = [0] * (N+1)
    
    for s in Ss: V[s] = 1
    
    if V[1]:
        print("Yes")
        return
    
    print(bfs(V, G))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()