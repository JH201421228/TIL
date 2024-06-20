import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1_000)


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
D = dict()
for i in range(1, M+1):
    D[input().rstrip()] = i

G = [[] for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(str, input().rstrip().split()))
    for s in temp[1:]:
        G[i].append(D[s])

C = [0] * (M+1)
isPossible = True
ans = 0
for i in range(1, N+1):
    V = [0] * (M+1)
    if not B(i):
        isPossible = False
    else:
        ans += 1

if isPossible:
    print('YES')
else:
    print('NO')
    print(ans)