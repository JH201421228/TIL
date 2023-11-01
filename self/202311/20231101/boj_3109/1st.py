import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(-1, 1), (0, 1), (1, 1)]


def dfs(x, y):

    if y == C-1:
        return True

    for dx, dy in delta:
        if 0 <= x+dx < R and 0 <= y+dy < C and MAP[x+dx][y+dy] == '.':
            MAP[x+dx][y+dy] = 'o'
            if dfs(x+dx, y+dy):
                return True
            # MAP[x+dx][y+dy] = '.'

R, C = map(int, input().split())
MAP = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
# for idx in range(R):
#
#     bfs(idx, 0)
# print(MAP)
flag = 0
ans = 0

for idx in range(R):
    # if MAP[idx][0] == 'o':
    #     continue
    # MAP[idx][0] = 'o'
    if dfs(idx, 0):
        ans += 1

    # for n_idx in range(idx+1, R):
    #     if MAP[n_idx][0] == '.':
    #         idx = n_idx
    #         break
    #     elif n_idx == R-1:
    #         idx = R-1
    # if flag:
    #     ans += 1
    #     flag = 0

    # else:
    #     print(idx)
    #     break
    #
    # for inner in MAP:
    #     print(inner)
    # print('--------------------------------------------------------------------')
print(ans)
# 4