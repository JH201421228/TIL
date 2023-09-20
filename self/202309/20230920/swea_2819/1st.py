import sys
sys.stdin = open('input.txt')

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def make_num(x, y, cnt, word):
    if cnt == 7:
        ans_set.add(word)
        return
    for dx, dy in delta:
        if 0 <= x+dx < 4 and 0 <= y+dy < 4:
            make_num(x+dx, y+dy, cnt+1, word + str(board[x+dx][y+dy]))


T = int(input())
for test in range(T):
    board = [list(map(int, input().split())) for _ in range(4)]
    # print(board)
    ans_set = set()
    for i in range(4):
        for j in range(4):
            result = ''
            make_num(i, j, 0, result)
    print(f'#{test + 1} {len(ans_set)}')
    # print(ans_set)