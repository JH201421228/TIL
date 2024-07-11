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


H, W = map(int, input().split())
N = []

for _ in range(H):
    N.append(list(map(int, input().split())))

N_ = [[0] * W for _ in range (H)]
cnt = 0

for i in range(H):
    for j in range(W):
        if N[i][j] == 3:
            cnt += 1
            N_[i][j] = [cnt]
        elif N[i][j] == 2:
            cnt += 2
            N_[i][j] = [cnt-1, cnt]

C = [0] * (cnt+1)
G = [[] for _ in range(cnt+1)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(H):
    for j in range(W):
        if not (i+j)%2 and N_[i][j]:
            for di, dj in delta:
                if i+di >= 0 and i+di < H and j+dj >= 0 and j+dj < W and N_[i+di][j+dj]:
                    if N[i][j] == 2 and N[i+di][j+dj] == 2:
                        continue
                    for k in N_[i][j]:
                        for l in N_[i+di][j+dj]:
                            G[k].append(l)

for i in range(H):
    for j in range(W):
        if not (i+j)%2 and N_[i][j]:
            for k in N_[i][j]:
                V = [0] * (cnt+1)
                if B(k):
                    C[k] = 1
                else:
                    print('HOMELESS')
                    exit(0)

for v in C[1:]:
    if not v:
        print('HOMELESS')
        exit(0)

print('HAPPY')