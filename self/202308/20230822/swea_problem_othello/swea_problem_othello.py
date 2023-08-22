import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]
    # print(info)
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    board[N // 2][N // 2] = 2
    # print(board)
    delta = [[1, 0], [0, 1], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    for i, j, bw in info:
        x = i - 1
        y = j - 1
        board[x][y] = bw
        for dx, dy in delta:
            flag = 0
            X = 0
            if 0 <= x + dx < N and 0 <= y + dy < N and board[x+dx][y+dy] and board[x+dx][y+dy] != bw : # 좌표가 보드 안에 있고, 상하좌우 중에 지금 놓은 돌의 색과 다른 돌이 놓여있다면.
                for k in range(2, N): # 다음 같은 색 돌을 만날 때 까지 가겠습니다.
                    if 0 <= x + k*dx < N and 0 <= y +k*dy < N:
                        if not board[x+k*dx][y+k*dy]:
                            break
                        elif board[x+k*dx][y+k*dy] == bw: # 해당 방향으로 가면서 좌표 안에 있고, 돌이 놓여있고, 같은색 돌을 만나면
                            flag = 1
                            X = k
                            break
                if flag:
                    for p in range(1, X):
                        board[x+p*dx][y+p*dy] = bw

        # for inner_board in board:
        #     print(inner_board)
        # print('--------------')

    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] == 2:
                cnt2 += 1
    print(f'#{test+1} {cnt1} {cnt2}')

