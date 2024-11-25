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


N = int(input())
info = [[]]
MAX = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    info.append(temp)
    MAX = max(MAX, temp[1], temp[3])

s, e = 0, MAX

while s <= e:
    mid = (s+e) >> 1
    cnt = 0

    G = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        cnt = 0
        a, b, c, d = info[i]

        if b <= mid:
            cnt += 1
            G[i].append(a)
        if d <= mid:
            cnt += 1
            G[i].append(c)

        if cnt == 0:
            break

    if cnt == 0:
        s = mid+1
        continue

    C = [0] * (2*N+1)
    for i in range(1, N+1):
        V = [0] * (2*N+1)
        if not B(i):
            s = mid+1
            break
    else:
        e = mid-1

if s > 1_000_000:
    print(-1)
else:
    print(s)