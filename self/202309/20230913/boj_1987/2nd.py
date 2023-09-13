import sys

sys.stdin = open('input.txt')

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def what_the_game(x, y, cnt):
    global ans
    if cnt > ans:
        ans = cnt

    for dx, dy in delta:
        if 0 <= x+dx < R and 0 <= y+dy < C:
            if [x+dx, y+dy] not in trace and board_info[x+dx][y+dy] not in alpha:
                trace.append([x+dx, y+dy])
                alpha.append(board_info[x+dx][y+dy])
                what_the_game(x+dx, y+dy, cnt+1)
                alpha.pop()
                trace.pop()


R, C = map(int, input().split())
board_info = [list(input()) for _ in range(R)]
trace = [[0, 0]]
alpha = [board_info[0][0]]
ans = 1
what_the_game(0, 0, 1)
print(ans)
