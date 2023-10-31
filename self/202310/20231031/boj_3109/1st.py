import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def dfs(x, y, status):
    global flag
    if y == C-1:
        flag = 1
        return

    for dx, dy in delta:
        if status and dx == -1:
            continue

        if 0 <= x+dx < R and 0 <= y+dy < C and MAP[x+dx][y+dy] == '.':
            MAP[x+dx][y+dy] = 'x'
            if dx == 1:
                dfs(x+dx, y+dy, 1)
            else:
                dfs(x+dx, y+dy, 0)
            if flag:
                break
            else:
                MAP[x+dx][y+dy] = '.'


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
    if MAP[idx][0] == 'x':
        continue
    MAP[idx][0] = 'x'
    dfs(idx, 0, 0)

    if flag:
        ans += 1
        flag = 0
    else:
        break

    for inner in MAP:
        print(inner)
    print('--------------------------------------------------------------------')
print(ans)
# 4