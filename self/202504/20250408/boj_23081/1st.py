import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_next_obj(direction_i, direction_j, cur_i, cur_j, target):
    res = 1

    init_i, init_j = cur_i, cur_j

    while True:
        cur_i += direction_i
        cur_j += direction_j

        if cur_i >= N or cur_j >= N:
            return 0, cur_i, cur_j

        if board[cur_i][cur_j] == 'W':
            res += 1
        elif board[cur_i][cur_j] == target:
            if target == '.':
                ans_board[cur_i][cur_j] += res
            else:
                if not direction_i:
                    ans_board[init_i][init_j-1] += res
                elif not direction_j:
                    ans_board[init_i-1][init_j] += res
                else:
                    ans_board[init_i-1][init_j-1] += res
            return res, cur_i, cur_j

        else:
            return 0, cur_i, cur_j


N = int(input())
board = [input().rstrip() for _ in range(N)]

ans_board = [[0] * N for _ in range(N)]

for i in range(N):
    j = 0
    while True:
        j += 1
        if j >= N: break

        if board[i][j-1] == '.' and board[i][j] == 'W':
            temp = find_next_obj(0, 1, i, j, 'B')
            j = temp[2]

        elif board[i][j-1] == 'B' and board[i][j] == 'W':
            temp = find_next_obj(0, 1, i, j, '.')
            j = temp[2]

for j in range(N):
    i = 0
    while True:
        i += 1
        if i >= N: break

        if board[i-1][j] == '.' and board[i][j] == 'W':
            temp = find_next_obj(1, 0, i, j, 'B')
            i = temp[1]

        elif board[i-1][j] == 'B' and board[i][j] == 'W':
            temp = find_next_obj(1, 0, i, j, '.')
            i = temp[1]

for i in range(N):
    j = 0
    while True:
        i += 1
        j += 1
        if i >= N or j >= N: break

        if board[i-1][j-1] == '.' and board[i][j] == 'W':
            temp = find_next_obj(1, 1, i, j, 'B')
            i, j = temp[1], temp[2]

        elif board[i-1][j-1] == 'B' and board[i][j] == 'W':
            temp = find_next_obj(1, 1, i, j, '.')
            i, j = temp[1], temp[2]

for j in range(1, N):
    i = 0
    while True:
        i += 1
        j += 1
        if i >= N or j >= N: break

        if board[i - 1][j - 1] == '.' and board[i][j] == 'W':
            temp = find_next_obj(1, 1, i, j, 'B')
            i, j = temp[1], temp[2]

        elif board[i - 1][j - 1] == 'B' and board[i][j] == 'W':
            temp = find_next_obj(1, 1, i, j, '.')
            i, j = temp[1], temp[2]

ans = 0
ans_x, ans_y = 0, 0
for i in range(N):
    for j in range(N):
        if ans_board[i][j] > ans:
            ans = ans_board[i][j]
            ans_x, ans_y = i, j

if ans:
    print(ans_y, ans_x)
    print(ans)
else:
    print("PASS")