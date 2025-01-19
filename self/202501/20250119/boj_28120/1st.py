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


N, K, X = map(int, input().split())
G = [[] for _ in range(N+1)]
W = [[0, i+1] + list(map(int, input().split())) for i in range(N)]

temp = tuple(map(int, input().split()))
for i in range(N):
    W[i][0] = temp[i]

W.sort(reverse=True)

for i in range(N):
    l = W[i]
    for n in l[3:]:
        for x in range((n-1)*X+1, n*X+1):
            G[i+1].append(x)

C = [0] * (X*K+1)
for i in range(1, N+1):
    V = [0] * (X*K+1)
    B(i)

ans_list = [[] for _ in range(K)]
for i in range(1, X*K+1):
    if C[i]:
        ans_list[(i-1)//X].append(W[C[i]-1][1])

for ans in ans_list:
    print(len(ans), *ans)