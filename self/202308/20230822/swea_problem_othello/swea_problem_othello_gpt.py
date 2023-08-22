import sys
sys.stdin = open('input.txt')



def main():
    sys.stdin = open('input.txt')

    Test = int(input())
    for test in range(Test):
        N, M = map(int, input().split())
        info = [list(map(int, input().split())) for _ in range(M)]

        board = initialize_board(N)
        update_board(board, info, N)

        cnt1, cnt2 = count_stones(board, N)
        print(f'#{test+1} {cnt1} {cnt2}')

def initialize_board(N):
    board = [[0] * N for _ in range(N)]
    mid = N // 2 - 1
    board[mid][mid] = 2
    board[mid][mid + 1] = 1
    board[mid + 1][mid] = 1
    board[mid + 1][mid + 1] = 2
    return board

def update_board(board, info, N):
    delta = [[1, 0], [0, 1], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    for i, j, bw in info:
        x = i - 1
        y = j - 1
        board[x][y] = bw
        for dx, dy in delta:
            flag = 0
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] and board[nx][ny] != bw:
                for k in range(2, N):
                    nkx, nky = x + k*dx, y + k*dy
                    if 0 <= nkx < N and 0 <= nky < N and board[nkx][nky] and board[nkx][nky] == bw:
                        flag = 1
                        X = k
                        break
                if flag:
                    for p in range(1, X):
                        board[x + p*dx][y + p*dy] = bw

def count_stones(board, N):
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] == 2:
                cnt2 += 1
    return cnt1, cnt2

if __name__ == "__main__":
    main()
