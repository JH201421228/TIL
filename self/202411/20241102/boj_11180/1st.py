import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

C = [0] * (N+1)
for i in range(1, N+1):
    V = [0] * (N+1)
    if not B(i):
        print('Impossible')
        exit(0)

for i in C[1:]:
    print(i)