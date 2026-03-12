import sys
sys.setrecursionlimit(100_000)
sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(cur, depth, V, G, D, A):
    D[cur] = depth
    
    for x, c in G[cur]:
        if not V[x]:
            V[x] = 1
            A[x][0][0] = cur
            A[x][0][1] = c
            
            dfs(x, depth+1, V, G, D, A)
    
    return


def LCA(a, b, D, A):
    if D[a] < D[b]: a, b = b, a
    
    cost = 0
    
    if D[a] != D[b]:
        diff = D[a] - D[b]
        
        for i in range(18):
            if diff & (1<<i):
                cost += A[a][i][1]
                a = A[a][i][0]
                
    if a == b: return cost, a
    
    for i in range(17, -1, -1):
        if A[a][i][0] != A[b][i][0]:
            cost += A[a][i][1]
            cost += A[b][i][1]
            a = A[a][i][0]
            b = A[b][i][0]
            
    cost += A[a][0][1]
    cost += A[b][0][1]
    
    return cost, A[a][0][0]


def solve():
    N = int(input())
    G = [[] for _ in range(N+1)]
    D = [0] * (N+1)
    V = [0] * (N+1)
    A = [[[0] * 2 for _ in range(18)] for _ in range(N+1)]
    
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))    
    
    V[1] = 1
    dfs(1, 0, V, G, D, A)
    
    for i in range(1, 18):
        for j in range(N+1):
            A[j][i][0] = A[A[j][i-1][0]][i-1][0]
            A[j][i][1] = A[j][i-1][1] + A[A[j][i-1][0]][i-1][1]
    
    for _ in range(int(input())):
        temp = tuple(map(int, input().split()))
        
        cost, node = LCA(*temp[1:3], D, A)
        
        if temp[0] == 1: print(cost)
        else:
            u, v, k = temp[1:]
            k -= 1
            
            if D[u]-D[node] < k:
                k = D[u]+D[v] - 2*D[node] - k
                u = v
            
            for i in range(17, -1, -1):
                if k & (1<<i):
                    u = A[u][i][0]
                    
            print(u)
            
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()