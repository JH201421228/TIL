import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

P = []
for _ in range(N):
    P.append(tuple(map(int, input().split())))

P.append(P[0])

ans = 0

for i in range(N):
    ans += P[i][0] * P[i+1][1]
    ans -= P[i][1] * P[i+1][0]

print(round(abs(ans) / 2, 1))