import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline



def dfs(n, F, E, V):
    V[n] = 1
    
    for x in F[n]:
        if not V[x]:
            dfs(x, F, E, V)
            
    for x in E[n]:
        for xx in E[x]:
            if not V[xx]:
                dfs(xx, F, E, V)
    
    return



def solve():
    N = int(input())
    M = int(input())
    
    F = [[] for _ in range(N+1)]
    E = [[] for _ in range(N+1)]
    V = [0] * (N+1)
    
    for _ in range(M):
        s, u, v = input().rstrip().split()
        
        u, v = int(u), int(v)
        
        if s == "F":
            F[u].append(v)
            F[v].append(u)
        else:
            E[u].append(v)
            E[v].append(u)
            

    ans = 0
    
    for n in range(1, N+1):
        if not V[n]:
            ans += 1
            dfs(n, F, E, V)
            
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()