import sys
from collections import deque
sys.stdin = open("input.txt")
sys.setrecursionlimit(500_000)
input = sys.stdin.readline


def scc(n, V, G, F, S):
    global o, group_n
    
    p = V[n] = o = o+1
    S.append(n)
    
    for x in G[n]:
        if V[x] == -1:
            p = min(p, scc(x, V, G, F, S))
        elif F[x] == -1:
            p = min(p, V[x])
            
    if p == V[n]:
        while S:
            c = S.pop()
            F[c] = group_n
            if c == n:
                break
        group_n += 1
    
    return p


def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    cash = [0] * (N+1)
    restaurant = [0] * (N+1)
    
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
    
    for idx in range(N):
        cash[idx+1] = int(input())
    
    s, p = map(int, input().split())
    
    temp = list(map(int, input().split()))
    
    for t in temp:
        restaurant[t] = 1
        
    V = [-1] * (N+1)
    F = [-1] * (N+1)
    S = []
    
    global o, group_n
    o = 0
    group_n = 1
    
    
    for n in range(1, N+1):
        if V[n] == -1: scc(n, V, G, F, S)
        
    group_cash = [0] * group_n
    group_graph = [[] for _ in range(group_n)]
    group_restaurant = [0] * group_n
    
    for n in range(1, N+1):
        group = F[n]
        group_cash[group] += cash[n]
        if restaurant[n]: group_restaurant[group] = 1
        
        for x in G[n]:
            if group != F[x]: group_graph[group].append(F[x])
    
    V = [0] * group_n
    s = F[s]
    V[s] = 1
    
    S = [s]

    while S:
        n = S.pop()
        for x in group_graph[n]:
            if not V[x]:
                V[x] = 1
                S.append(x)
                
    indegree = [0] * group_n
    for n in range(1, group_n):
        if not V[n]: continue
        for x in group_graph[n]:
            if V[x]: indegree[x] += 1
            
    dp = [-1] * group_n
    dp[s] = group_cash[s]
    
    q = deque([s])
    
    while q:
        n = q.popleft()
        
        for x in group_graph[n]:
            dp[x] = max(dp[x], dp[n] + group_cash[x])
                
            indegree[x] -= 1
            
            if not indegree[x]: q.append(x)
            
    ans = 0
    
    for idx in range(1, group_n):
        if group_restaurant[idx]: ans = max(ans, dp[idx])
        
    print(ans)

    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()