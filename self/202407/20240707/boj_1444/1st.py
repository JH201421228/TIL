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


I = list(map(str, input().rstrip()))
for idx in range(len(I)):
    I[idx] = ord(I[idx])

G = [[] for _ in range(26*2+1)]
C = [0] * (26*2+1)

for idx in range(len(I)-1):
    if I[idx] <= 90 and I[idx+1] >= 97:
        G[I[idx]-64].append(I[idx+1]-96+26)
    elif I[idx+1] <= 90 and I[idx] >= 97:
        G[I[idx] - 96+26].append(I[idx + 1] - 64)

ans = 0
for i in range(1, 26*2+1):
    V = [0] * (26*2+1)
    if B(i):
        ans += 1

print(ans)