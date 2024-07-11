import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1_500)


def B(n):
    for x in G[n]:
        if V[x-26*26]:
           continue
        V[x-26*26] = 1

        if not C[x-26*26] or B(C[x-26*26]):
            C[x-26*26] = n
            return True

    return False


def T(X, Y):
    if X <= 26:
        return (X-1)*26+Y-26
    return (X-1)*26+Y


word = list(map(str, input().rstrip()))
N = len(word)

for i in range(N):
    if ord(word[i]) <= 90:
        word[i] = ord(word[i]) - 64
    else:
        word[i] = ord(word[i]) - 96 + 26

G = [[] for _ in range(26*26+1)]
C = [0] * (26*26+1)

S, E = T(word[0], word[1]), T(word[N-2], word[N-1])
if S == E:
    ans = 1
else:
    ans = 2

for i in range(1, N-3):
    a, b = T(word[i], word[i+1]), T(word[i+1], word[i+2])

    if a == S or a == E or b == S or b == E:
        continue

    if a <= 26*26:
        G[a].append(b)
    else:
        G[b].append(a)

for i in range(1, 26*26+1):
    V = [0] * (26*26+1)
    if B(i):
        ans += 1

print(ans)