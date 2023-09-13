import sys

sys.stdin = open('input.txt')

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def what_the_game(x, y, cnt):

    global ans
    if cnt > ans:
        ans = cnt

    for dx, dy in delta:
        if 0 <= x+dx < R and 0 <= y+dy < C:
            if not check_list[board[x+dx][y+dy]]:
                check_list[board[x+dx][y+dy]] = 1
                # trace.append([x+dx, y+dy])
                what_the_game(x+dx, y+dy, cnt + 1)
                # trace.pop()
                check_list[board[x+dx][y+dy]] = 0



R, C = map(int, input().split())
board = [[0] * C for _ in range(R)]
for i in range(R):
    temp = list(input())
    for j in range(C):
        board[i][j] = ord(temp[j]) - ord('A')
check_list = [0] * 26
check_list[board[0][0]] = 1
# trace = [[0, 0]]
ans = 1
what_the_game(0, 0, 1)
print(ans)