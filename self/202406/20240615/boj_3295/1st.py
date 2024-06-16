import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1_000)


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if C[x] == -1 or B(C[x]):
            C[x] = n
            return True

    return False


for _ in range(int(input())):
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)

    C = [-1] * N
    ans = 0
    for i in range(N):
        V = [0] * N
        if B(i):
            ans += 1

    print(ans)