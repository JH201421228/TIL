import sys
sys.setrecursionlimit(100_000)
sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(cur, depth, V, G, D, A):
    D[cur] = depth
    
    for x in G[cur]:
        if not V[x]:
            V[x] = 1
            A[x][0] = cur
            
            dfs(x, depth+1, V, G, D, A)
    
    return


def LCA(a, b, D, A):
    if D[a] < D[b]:
        a, b = b, a
        
    if D[a] != D[b]:
        diff = D[a] - D[b]
        for i in range(18):
            if diff & (1<<i): a = A[a][i]
            
    if a == b: return a
    
    for i in range(17, -1, -1):
        if A[a][i] != A[b][i]:
            a, b = A[a][i], A[b][i]
    
    return A[a][0]


def solve():
    N = int(input())
    G = [[] for _ in range(N+1)]
    V = [0] * (N+1)
    D = [0] * (N+1)
    A = [[0] * 18 for _ in range(N+1)]
    
    for _ in range(N-1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        
    V[1] = 1
    dfs(1, 0, V, G, D, A)

    for i in range(1, 18):
        for j in range(1, N+1):
            A[j][i] = A[A[j][i-1]][i-1]
        
    M = int(input())
    
    for _ in range(M):
        q1, q2 = map(int, input().split())
        print(LCA(q1, q2, D, A))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()