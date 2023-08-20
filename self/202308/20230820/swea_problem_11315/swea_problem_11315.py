import sys
sys.stdin = open('input.txt')


def finder(N):
    for i in range(N):
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        for j in range(N):
            if board[i][j] == 'o':
                cnt1 += 1
            else:
                cnt1 = 0

            if trans_board[i][j] == 'o':
                cnt2 += 1
            else:
                cnt2 = 0

            if cnt1 == 5 or cnt2 == 5:
                return 'YES'

            if board[i][j] == 'o':
                cnt3 = 1
                for x in range(1, 5):
                    if i+x < N and j+x < N and board[i+x][j+x] == 'o':
                        cnt3 += 1
                        if cnt3 == 5:
                            return 'YES'
                    else:
                        cnt3 = 0
                        break
            if board[i][j] == 'o':
                cnt4 = 1
                for x in range(1, 5):
                    if i+x < N and 0 <= j-x and board[i+x][j-x] == 'o':
                        cnt4 += 1
                        if cnt4 == 5:
                            return 'YES'
                    else:
                        cnt4 = 0
                        break


    return 'NO'


Test = int(input())
for test in range(Test):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    trans_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            trans_board[i][j] = board[j][i]

    # print(board)
    # print(trans_board)
    print(f'#{test + 1} {finder(N)}')