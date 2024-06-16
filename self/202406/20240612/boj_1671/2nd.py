import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in range(R):
        if V[x] or x == n:
            continue
        if not(S[n][0] >= S[x][0] and S[n][1] >= S[x][1] and S[n][2] >= S[x][2]):
            continue
        V[x] = 1

        if C[x] == -1 or B(C[x]):
            C[x] = n
            return True

    return False


N = int(input())
S = set()
for _ in range(N):
    S.add(tuple(map(int, input().split())))

S = [*S]
R = len(S)
C = [-1] * R
for i in range(R):
    for _ in range(2):
        V = [0] * R
        B(i)

ans = 0
for i in range(R):
    if C[i] == -1:
        ans += 1

print(ans)