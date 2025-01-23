import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


R, C = map(int, input().split())
M = [list(map(str, input().rstrip())) for _ in range(R)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
c = dict()

for i in range(R):
    for j in range(C):
        if M[i][j] == 'X':
            c[(i, j)] = 0
            for di, dj in delta:
                ii, jj = i+di, j+dj
                if ii >= 0 and ii < R and jj >= 0 and jj < C:
                    if M[ii][jj] == '.':
                        c[(i, j)] += 1
                else:
                    c[(i, j)] += 1

ans_list = []
max_i, min_i, max_j, min_j = -float("inf"), float("inf"), -float("inf"), float("inf")
for k, v in c.items():
    if v < 3:
        max_i, min_i, max_j, min_j = max(max_i, k[0]), min(min_i, k[0]), max(max_j, k[1]), min(min_j, k[1])
        ans_list.append(k)

ans = [['.']*(max_j-min_j+1) for _ in range(max_i-min_i+1)]

for t in ans_list:
    ans[t[0]-min_i][t[1]-min_j] = 'X'

for i in ans:
    print(''.join(i))