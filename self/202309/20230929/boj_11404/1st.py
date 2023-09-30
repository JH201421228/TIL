import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
M = int(input())
ans_list = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    start, end, point = map(int, input().split())
    ans_list[start-1][end-1] = min(point, ans_list[start-1][end-1])
# print(ans_list)
for k in range(N):
    for j in range(N):
        for i in range(N):
            if i == j:
                ans_list[i][j] = 0
            else:
                if ans_list[i][j] > ans_list[i][k] + ans_list[k][j]:
                    ans_list[i][j] = ans_list[i][k] + ans_list[k][j]
for i in range(N):
    for j in range(N):
        if ans_list[i][j] == float('inf'):
            ans_list[i][j] = 0

for inner in ans_list:
    print(*inner)