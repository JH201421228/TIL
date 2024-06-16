import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in range(1, N+1):
        if V[x] or x == n:
            continue
        if not(S[n][0] >= S[x][0] and S[n][1] >= S[x][1] and S[n][2] >= S[x][2]):
            continue
        if (S[n][0] == S[x][0] and S[n][1] == S[x][1] and S[n][2] == S[x][2]) and x > n:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


N = int(input())
S = [[]]
for _ in range(N):
    S.append(list(map(int, input().split())))

C = [0] * (N+1)
for i in range(1, N+1):
    for _ in range(2):
        V = [0] * (N+1)
        B(i)

ans = 0
for i in range(1, N+1):
    if not C[i]:
        ans += 1

print(ans)
print(C)
