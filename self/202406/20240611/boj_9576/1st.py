import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(2_000)


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


for _ in range(int(input())):
    N, M = map(int, input().split())
    G = [[]]
    for _ in range(M):
        a, b = map(int, input().split())
        G.append(list(range(a, b+1)))
    C = [0] * (N+1)

    for i in range(1, M+1):
        V = [0] * (N+1)
        B(i)

    ans = 0
    for i in range(1, N+1):
        if C[i]:
            ans += 1

    print(ans)