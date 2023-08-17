import sys
from pprint import pprint as print
# sys.setrecursionlimit(1500000)
sys.stdin = open('input.txt')

def only_one_zero(): # 0이 한개인 부분만 검사하고 찾을시 해당 부분을 나타내는 인덱스를 반환
    global cnt
    cnt = 0

    for i in range(9):

        if 0 in puzzle[i] and puzzle[i].count(0) == 1:
            count[i] = 1
            cnt = 1
            return [i, puzzle[i].index(0)]
        else:
            count[i] = 0


    for i in range(9):

        if 0 in puzzle_trans[i] and puzzle_trans[i].count(0) == 1:
            count[i+9] = 1
            cnt = 2
            return [puzzle_trans[i].index(0), i]
        else:
            count[i] = 0


def puzzle_breaker():
    if cnt == 0:
        return
    point = only_one_zero()
    x = point[0]
    y = point[1]
    if cnt == 1:
        puzzle[x][y] = 45 - sum(puzzle[x])
        puzzle_trans[y][x] = 45 - sum(puzzle[x])
    elif cnt == 2:
        puzzle[x][y] = 45 - sum(puzzle[i][y] for i in range(9))
        puzzle_trans[y][x] = 45 - sum(puzzle[i][y] for i in range(9))
    print(puzzle)
    puzzle_breaker()

puzzle = [list(map(int, input().split())) for _ in range(9)]
puzzle_trans = [[0] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        puzzle_trans[i][j] = puzzle[j][i]
count = [0] * 27
cnt = 4


puzzle_breaker()
print(puzzle)
