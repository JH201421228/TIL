import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n, C, G):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x], C, G):
            C[x] = n
            return True

    return False


N, M, K1, K2 = map(int, input().split())
G1, G2 = [[] for _ in range(N+1)], [[] for _ in range(N+1)]
C1, C2 = [0] * (M+1), [0] * (M+1)

for _ in range(K1):
    a, b = map(int, input().split())
    G1[a].append(b)

for _ in range(K2):
    a, b = map(int, input().split())
    G2[a].append(b)

p1, p2 = 0, 0

for i in range(1, N+1):
    V = [0] * (M+1)
    if B(i, C1, G1):
        p1 += 1

    V = [0] * (M+1)
    if B(i, C2, G2):
        p2 += 1

if p2 > p1:
    print('네 다음 힐딱이')
else:
    print('그만 알아보자')