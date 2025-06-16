import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# ans = [(개수, 행, 열), ...]

def get_cnt(x, y, cnt, N):
    if x < 0 or y < 0: return 0

    if x >= N: x = N-1
    if y >= N: y = N-1

    return cnt[x][y]

def solve():
    N, D = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[0] * N for _ in range(N)]

    cnt[0][0] = board[0][0]
    for i in range(1, N):
        cnt[i][0] = cnt[i-1][0] + board[i][0]
        cnt[0][i] = cnt[0][i-1] + board[0][i]

    for i in range(1, N):
        for j in range(1, N):
            cnt[i][j] = cnt[i][j-1]+cnt[i-1][j]-cnt[i-1][j-1]+board[i][j]

    res = []

    for i in range(N):
        for j in range(N):
            if not board[i][j] : res.append((get_cnt(i+D, j+D, cnt, N)+get_cnt(i-D-1, j-D-1, cnt, N)-get_cnt(i-D-1, j+D, cnt, N)-get_cnt(i+D, j-D-1, cnt, N), i+1, j+1))

    res.sort()

    if res[0][0]:
        print(*res[0][1:])
        print(res[0][0])
    else:
        print(*res[0][1:])



    return


if __name__ == "__main__":
    solve()