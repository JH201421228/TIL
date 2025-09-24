import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(n, V, G):
    q = deque([n])
    V[n] = 1

    vertex = len(G[n])
    node = 1

    while q:
        n = q.popleft()
        
        for x in G[n]:
            if not V[x]:
                q.append(x)
                V[x] = 1
                node += 1
                vertex += len(G[x])

    # print(vertex)
    # print(node)
    return node == 1 or vertex//2 == node-1


def solve(N, M):
    G = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    ans = 0

    V = [0] * (N+1)
    for n in range(1, N+1):
        if not V[n]:
            if bfs(n, V, G): ans += 1

    if not ans:
        return "No trees."
    elif ans == 1:
        return "There is one tree."
    else:
        return f"A forest of {ans} trees."


def main():
    z = 0
    while True:
        z += 1
        N, M = map(int, input().split())
        if not N and not M: break
        print(f"Case {z}:", solve(N, M))
    return


if __name__ == "__main__":
    main()