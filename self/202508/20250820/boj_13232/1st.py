import sys
sys.setrecursionlimit(5_000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def scc(n):
    global V, O, G, F, S, ans

    p = V[n] = O = O + 1
    S.append(n)

    for x in G[n]:
        if not V[x]: p = min(p, scc(x))
        elif not F[x]: p = min(p, V[x])

    if p == V[n]:
        tmp = 0
        while S:
            o = S.pop()
            tmp += 1

            F[o] = 1

            if o == n: break

        ans = max(ans, tmp)

    return p

def solve():
    global V, O, G, F, S, ans

    D = int(input())
    L = int(input())
    G = [[] for _ in range(D+1)]

    for _ in range(L):
        u, v = map(int, input().split())
        G[u].append(v)

    V = [0] * (D+1)
    F = [0] * (D+1)
    ans = 0
    O = 0
    S = []

    for n in range(1, D+1):
        if not V[n]: scc(n)

    print(ans)

    return


if __name__ == "__main__":
    solve()