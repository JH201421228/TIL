import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def init():
    while True:
        N = int(input())
        if N == 0: break

        solve(N)

    return


def scc(n, G, V, F, S, result):
    global O

    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]: p = min(p, scc(x, G, V, F, S, result))
        elif not F[x]: p = min(p, V[x])

    if p == V[n]:
        temp = []

        while S:
            o = S.pop()
            F[o] = 1
            temp.append(chr(o+64))

            if o == n:
                temp.sort()
                result.append(temp)
                break

    return p


def solve(N):
    global O

    G = [[] for _ in range(27)]
    V = [0] * 27
    F = [0] * 27
    O = 0
    S = []
    U = [0] * 27
    result = []

    for _ in range(N):
        choices = list(input().rstrip().split())
        for idx in range(5):
            G[ord(choices[idx])-64].append(ord(choices[-1])-64)
            U[ord(choices[idx])-64] = 1

    for n in range(1, 27):
        if not V[n] and U[n]: scc(n, G, V, F, S, result)

    result.sort()
    for res in result:
        print(*res)

    print()
    return


if __name__ == "__main__":
    init()