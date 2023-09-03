import sys
sys.stdin = open('input.txt')

def check(num, i, j):
    for k in range(9):
        if Board[i][k] == num:
            return False
        if Board[k][j] == num:
            return False
    M = (i//3)*3
    N = (j//3)*3
    for m in range(M, M+3):
        for n in range(N, N+3):
            if Board[m][n] == num:
                return False
    return True

def DFS(N):
    if N == 0:
        for inner in Board:
            print(*inner)
        exit(0)

    i, j = Blank.pop()
    for num in range(1, 10):
        if check(num, i, j):
            Board[i][j] = num
            # print(num)
            DFS(N-1)
            Board[i][j] = 0
    return False

Board = [list(map(int, input().split())) for _ in range(9)]
Blank = []
for i in range(9):
    for j in range(9):
        if Board[i][j] == 0:
            Blank.append((i, j))
N = len(Blank)
DFS(N)
print(Board)