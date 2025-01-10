import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(5_000)
input = sys.stdin.readline


def scc(n):
    global O, cnt

    S.append(n)
    p = V[n] = O = O+1

    for x in G[n]:
        if not V[x]:
            p = min(scc(x), p)
        elif not F[x]:
            p = min(V[x], p)

    if p == V[n]:
        cnt += 1
        while S:
            out = S.pop()
            F[out] = cnt
            if out == n:
                break

    return p


while True:
    temp = list(map(int, input().split()))
    if not temp[0]:
        break

    N, M = temp

    G = [[] for _ in range(N+1)]
    Gs = [[] for _ in range(N+1)]
    temp = list(map(int, input().split()))

    for i in range(M):
        G[temp[2*i]].append(temp[2*i+1])

        Gs[temp[2*i]].append(temp[2*i+1])
        Gs[temp[2*i+1]].append(temp[2*i])

    cnt = 0
    O = 0
    S = []
    V = [0] * (N+1)
    F = [0] * (N+1)

    for n in range(1, N+1):
        if not V[n]:
            flag = cnt+1
            scc(n)

    Vc = [0] * (cnt+1)
    ans_list = []
    ans = []

    def checker(n, flag):
        Vt[n] = 1

        for x in G[n]:
            if not Vt[x]:
                if F[x] != flag:
                    return False

                if not checker(x, flag):
                    return False

        return True

    for n in range(1, N+1):
        if not Vc[F[n]]:
            Vc[F[n]] = 1
            Vt = [0] * (N+1)
            if checker(n, F[n]):
                ans_list.append(F[n])

    for n in range(1, N+1):
        if F[n] in ans_list:
            ans.append(n)

    print(*ans)
    # print(ans_list)
    # print(F)
    # print('=' * 50)