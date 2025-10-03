import sys
sys.setrecursionlimit(300_000)
sys.stdin = open("input.txt")
input = sys.stdin.readline


def set_inner(n, inner, nodes, G):
    nodes[n] = 1
    
    for x, d in G[n]:
        if not nodes[x]:
            set_inner(x, inner , nodes, G)
            nodes[n] += nodes[x]
            inner[n] += inner[x] + nodes[x] * d
    
    return


def set_outer(n, inner, outer, nodes, V, G, N):
    V[n] = 1
    
    for x, d in G[n]:
        if not V[x]:
            outer[x] = outer[n] + (N - nodes[n]) * d + inner[n] - (inner[x] + nodes[x] * d) + (nodes[n] - nodes[x]) * d
            set_outer(x, inner, outer, nodes, V, G, N)
            
    return


def solve():
    N = int(input())
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v, d = map(int, input().split())
        G[u].append((v, d))
        G[v].append((u, d))
    
    nodes = [0] * (N+1)
    inner = [0] * (N+1)
    outer = [0] * (N+1)
    
    set_inner(1, inner, nodes, G)
    V = [0] * (N+1)
    set_outer(1, inner, outer, nodes, V, G, N)
    
    ans = '\n'.join(str(inner[i] + outer[i]) for i in range(1, N+1))
    
    sys.stdout.write(ans)
    
    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()