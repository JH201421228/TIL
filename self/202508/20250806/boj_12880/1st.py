import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def scc(n, V, F, G, S):
    global O
    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]: p = min(p, scc(x, V, F, G, S))
        elif not F[x]: p = min(p, V[x])

    if V[n] == p:
        while S:
            o = S.pop()
            F[o] = 1

            if o == n: break

    return p


def solve():
    global O

    N = int(input())

    if N == 1:
        print(0)
        return

    weights_map = [list(map(int, input().split())) for _ in range(N)]
    weights = set()

    for i in range(N):
        for j in range(N):
            if i == j: continue

            weights.add(weights_map[i][j])

    weights = list(weights)
    weights.sort()

    interval = float("inf")

    s, e, length = 0, 0, len(weights)

    while True:
        if weights[e] - weights[s] >= interval:
            if e > s: s += 1
            elif e == length - 1: break
            else: e += 1

            continue

        S = []
        V = [0] * (N+1)
        F = [0] * (N+1)
        G = [[] for _ in range(N+1)]
        O = 0

        for i in range(N):
            for j in range(N):
                if i == j: continue
                if weights[s] <= weights_map[i][j] <= weights[e]:
                    G[i+1].append(j+1)

        scc(1, V, F, G, S)

        isPossible = True
        for x in F[1:]:
            if not x:
                isPossible = False
                break

        if not isPossible:
            if e == length-1:
                break
            e += 1
        else:
            interval = weights[e] - weights[s]
            if s == e:
                if e == length-1:
                    break
                else:
                    e += 1
            else:
                s += 1

    print(interval)

    return


if __name__ == "__main__":
    solve()