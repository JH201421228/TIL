import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def i_am_ironman(char):
    matrix = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if (i+j) % 2:
                check = char == board[i-1][j-1]
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1] + check
            else:
                check = char != board[i - 1][j - 1]
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1] + check
    ans = sys.maxsize
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            ans = min(ans, matrix[i+K-1][j+K-1] - matrix[i-1][j+K-1] - matrix[i+K-1][j-1] + matrix[i-1][j-1])
    return ans

N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
# print(board)
# print(i_am_ironman('B'))
# print(i_am_ironman('W'))
print(min(i_am_ironman('W'), i_am_ironman('B')))