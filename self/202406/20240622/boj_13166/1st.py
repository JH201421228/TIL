import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(200_000)


def B(n, v):
    for x, y in G[n]:
        if y > v:
            continue
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x], v):
            C[x] = n
            return True

    return False


N = int(input())
G = [[] for _ in range(N+1)]

for i in range(1, N+1):
    a, b, c, d = map(int, input().split())
    G[i].append((a, b))
    G[i].append((c, d))

isPossible = False
start, end = 0, 1_000_000

while start <= end:
    mid = (start + end) >> 1
    C = [0] * (2 * N + 1)
    isAvailable = True

    for i in range(1, N+1):
        V = [0] * (2*N+1)
        if not B(i, mid):
            isAvailable = False
            break

    if isAvailable:
        isPossible = True
        end = mid - 1
    else:
        start = mid + 1

if isPossible:
    print(start)
else:
    print(-1)