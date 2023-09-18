import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
A_matrix = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B_matrix = [list(map(int, input().split())) for _ in range(M)]

# for inner in A_matrix:
#     print(inner)
# for inner in B_matrix:
#     print(inner)

ans_matrix = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            ans_matrix[i][j] += A_matrix[i][k] * B_matrix[k][j]
for inner in ans_matrix:
    print(*inner)
