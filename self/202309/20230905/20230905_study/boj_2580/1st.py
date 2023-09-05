import sys
sys.stdin = open('input.txt')


def checker(i, j, n):
    for idx in range(9): 
        if idx != j:
            if sudoku[i][idx] == n:
                return False
        if idx != i:
            if sudoku[idx][j] == n:
                return False
    # 해당 좌표의 열과 행에 n과 같은 값이 있다면 False를 반환

    for x in range(i//3 * 3, i//3 * 3 + 3):
        for y in range(j//3 * 3, j//3 * 3 + 3):
            if x != i and y != j:
                if sudoku[x][y] == n:
                    return False
    # n이 들어있는 스도쿠의 3x3 지역에 n과 같은 값이 있다면 False를 반환

    return True # 끝까지 통과하면 True를 반환


def this_game(start):
    if start == len(start_point): # start의 값이 해당 리스트의 길이와 같아지면 중지
        for inner in sudoku: # 답을 출력하고
            print(*inner)
        # print(sudoku)
        exit(0) # 강제 종료

    now_i, now_j = start_point[start] # 0의 좌표가 기록된 리스트에서 start 인덱스에 해당하는 좌표값을 받아옴
    for num in range(9, 0, -1): # 1 ~ 9 까지의 값을 넣어봄
        sudoku[now_i][now_j] = num # 0이 있는 자리를 일단 숫자를 채우고
        if checker(now_i, now_j, num): # 유효한 값이라면,
            this_game(start+1) # 다음 start 인덱스에 대해 함수 호출
        sudoku[now_i][now_j] = 0 # 재귀되어 돌아올 시, 해당 값을 0으로 돌려놓음


sudoku = [list(map(int, input().split())) for _ in range(9)] # 스도쿠 인풋을 받아옴
start_point = [] # 스도쿠 리스트를 순회하며 0인 지점의 좌표를 받아올 리스트 생성
for idx_i in range(9):
    for idx_j in range(9):
        if not sudoku[idx_i][idx_j]:
            start_point.append([idx_i, idx_j]) # 스도쿠를 순회하며 0인 지점을 저장
this_game(0)
# print(sudoku)