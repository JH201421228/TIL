import sys
sys.stdin = open('input.txt')

def checker1():
    for inner_list in puzzle:
        if len(inner_list) != len(set(inner_list)):
            return False
    return True


def checker2():
    for inner_list in trans_puzzle:
        if len(inner_list) != len(set(inner_list)):
            return False
    return True


def checker3():
    for i in range(3):
        for j in range(3):
            if puzzle[3*i][3*j] + puzzle[3*i][3*j+1] + puzzle[3*i][3*j+2] + puzzle[3*i+1][3*j] + puzzle[3*i+1][3*j+1] + puzzle[3*i+1][3*j+2] + puzzle[3*i+2][3*j] + puzzle[3*i+2][3*j+1] + puzzle[3*i+2][3*j+2] != 45:
                return False
    return True


Test = int(input())
for test in range(Test):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    trans_puzzle = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            trans_puzzle[i][j] = puzzle[j][i]

    if checker1() and checker2() and checker3():
        print(f'#{test+1} 1')
    else:
        print(f'#{test + 1} 0')

