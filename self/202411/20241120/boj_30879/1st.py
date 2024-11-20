import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(200_000)
input = sys.stdin.readline


def scc(n):
    global O, cnt
    p = V[n] = O = O+1
    S.append(n)

    for x in G[n]:
        if not V[x]:
            p = min(p, scc(x))
        elif not F[x]:
            p = min(p, V[x])

    if p == V[n]:
        cnt += 1
        while S:
            out = S.pop()
            F[out] = cnt
            if out == n:
                break

    return p


N = int(input())
G = [[] for _ in range(2*100_000+1)]

done = False

for _ in range(N):
    temp = list(map(int, input().split()))

    if temp[0] == 1:
        G[-temp[1]].append(temp[2])
        G[-temp[2]].append(temp[1])
    else:
        if not done:
            V = [0] * (200_001)
            F = [0] * (200_001)
            S = []
            O = 0
            cnt = 0
            for i in range(-100_000, 100_001):
                if i and not V[i]:
                    scc(i)

            for i in range(1, 100_001):
                if F[i] and F[i] == F[-i]:
                    done = True
                    print('NO DINNER')
                    break
            else:
                print('YES DINNER')
        else:
            print('NO DINNER')