import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

for idx in range(1, M):
    B[0][idx] += B[0][idx-1]

for idx in range(1, N):
    B[idx][0] += B[idx-1][0]

for i in range(1, N):
    for j in range(1, M):
        B[i][j] += max(B[i][j-1], B[i-1][j])

print(B[-1][-1])