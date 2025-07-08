import sys
sys.setrecursionlimit(50_000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def scc(n):
    global O, S, G, V, F, C, ans_list

    p = V[n] = O = O+1
    S.append(n)

    x = G[n]
    if not V[x]: p = min(p, scc(x))
    elif not F[x]: p = min(p, V[x])

    if p == V[n]:
        temp = []
        while S:
            o = S.pop()
            temp.append(o)
            F[o] = -1

            if o == n:
                ans_list.append(temp)
                break

    return p


def get_next(n):
    res = n
    while n:
        res += n%10
        n //= 10

    return res


def get_max_value(n):
    global F, G

    # V = [0] * (N+1)
    #
    # for n in range(1, N+1):
    #     if not V[n]:
    #         temp = []
    #         checker = [0] * (N+1)
    #         while True:
    #             temp.append(n)
    #             checker
    #
    #             if F[n] != 1:
    #                 v = F[n]
    #                 break
    #
    #             n = G[n]
    #
    #         while temp:
    #             V[temp.pop()] = v
    #             v += 1

    x = G[n]
    if x == n:
        F[n] = 1
    elif F[x] != 1:
        F[n] = F[x]+1
    else:
        F[n] = get_max_value(x)+1

    return F[n]


def solve():
    N = int(input())
    global O, S, G, V, F, C, ans_list

    G = [0] * (N+1)
    for n in range(1, N+1):
        x = get_next(n)
        if x < N+1: G[n] = x
        elif not x % N: G[n] = N
        else: G[n] = x % N

    ans_list = []
    S = []
    V = [0] * (N+1)
    F = [0] * (N+1)
    O = 0
    C = 0

    for n in range(1, N+1):
        if not V[n]: scc(n)

    for temp in ans_list:
        val = len(temp)
        for v in temp:
            F[v] = val

    for n in range(1, N+1):
        if F[n] != 1: continue
        get_max_value(n)

    print(max(F))

    return


if __name__ == "__main__":
    solve()