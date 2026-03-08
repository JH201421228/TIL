import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(cur, depth, G, V, D, A):
    D[cur] = depth
    
    for nxt, cost in G[cur]:
        if not V[nxt]:
            V[nxt] = 1
            A[nxt][0][0] = cur
            A[nxt][0][1] = cost
            A[nxt][0][2] = cost
            
            dfs(nxt, depth+1, G, V, D, A)
            
    return


def LCA(a, b, D, A):
    if D[a] < D[b]: a, b = b, a
    
    min_res, max_res = float("inf"), -float("inf")
    
    if D[a] != D[b]:
        diff = D[a] - D[b]
        for i in range(18):
            if diff & (1<<i):
                max_res = max(max_res, A[a][i][1])
                min_res = min(min_res, A[a][i][2])
                a = A[a][i][0]
    
    if a == b:
        return (min_res if min_res != float("inf") else 0, max_res if max_res != -float("inf") else 0)

    for i in range(17, -1, -1):
        if A[a][i][0] != A[b][i][0]:
            max_res = max(max_res, A[a][i][1], A[b][i][1])
            min_res = min(min_res, A[a][i][2], A[b][i][2])
            a, b = A[a][i][0], A[b][i][0]

    min_res = min(min_res, A[a][0][1], A[b][0][1])
    max_res = max(max_res, A[a][0][2], A[b][0][2])

    return (min_res if min_res != float("inf") else 0, max_res if max_res != -float("inf") else 0)


def solve():
    N = int(input())
    D = [0] * (N+1)
    V = [0] * (N+1)
    A = [[[0, -float("inf"), float("inf")] for _ in range(18)] for _ in range(N+1)]
    G = [[] for _ in range(N+1)]
    
    for _ in range(N-1):
        u, v, c = map(int, input().split())
        G[u].append((v, c))
        G[v].append((u, c))
    
    V[1] = 1
    dfs(1, 0, G, V, D, A)
    
    for i in range(1, 18):
        for j in range(1, N+1):
            A[j][i][0] = A[A[j][i-1][0]][i-1][0]
            A[j][i][1] = max(A[A[j][i-1][0]][i-1][1], A[j][i-1][1])
            A[j][i][2] = min(A[A[j][i-1][0]][i-1][2], A[j][i-1][2])
    
    for _ in range(int(input())):
        u, v = map(int, input().split())
        print(*LCA(u, v, D, A))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()