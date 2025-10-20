import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    G = [[] for _ in range(N+1)]

    for _ in range(N-1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    if N < 5:
        print((N * (N-1)) // 2 - (N-1))
        print(1)
        for u in range(1, N+1):
            for v in range(1, N+1):
                if u != v and v not in G[u]:
                    print(u, v)
                    G[u].append(v)
                    G[v].append(u)
    else:
        print(N-1 - len(G[1]))
        print(2)
        for n in range(2, N+1):
            if n not in G[1]:
                print(1, n)

    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()