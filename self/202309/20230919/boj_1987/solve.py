import sys
sys.stdin = open('input.txt')

# 말은 상하 좌우 인접한 칸으로 이동 가능함
# 말이 이동할 수 있는 범위 델타 탐색
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def what_the_game(x, y, cnt):

    global ans
    if cnt > ans: # 더 멀리 갈 수 있다면
        ans = cnt # 값을 변경

    for dx, dy in delta:
        if 0 <= x+dx < R and 0 <= y+dy < C:
            if not check_list[board[x+dx][y+dy]]: # 해당 알파벳을 방문하지 않았다면
                check_list[board[x+dx][y+dy]] = 1 # 알파벳 방문 체크
                # trace.append([x+dx, y+dy])
                what_the_game(x+dx, y+dy, cnt + 1) # 다음 탐색 진행
                # trace.pop()
                check_list[board[x+dx][y+dy]] = 0 # 재귀로 돌아오면 알파벳 방문 체크 리셋


R, C = map(int, input().split())
board = [[0] * C for _ in range(R)]
for i in range(R):
    temp = list(input())
    for j in range(C):
        board[i][j] = ord(temp[j]) - ord('A') # 숫자 값으로 변경
check_list = [0] * 26 # 26개의 알파벳을 저장할 리스트 생성
check_list[board[0][0]] = 1 # 말은 반드시 해당 좌표에서 움직이기 시작함
# trace = [[0, 0]]
ans = 1
what_the_game(0, 0, 1)
print(ans)