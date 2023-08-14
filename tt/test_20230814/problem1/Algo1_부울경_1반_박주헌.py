import sys
sys.stdin = open('input.txt')
##############################################


def how_many_top(N): # 봉우리가 몇개 있는지 확인할 함수를 정의합니다.
    ans = 0 # 봉우리의 개수를 나타내는 변수입니다.
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 델타 탐색
    for x in range(N):
        for y in range(N):
            for dx, dy in delta:
                if 0 <= x+dx < N and 0 <= y+dy < N:
                    if matrix[x][y] <= matrix[x+dx][y+dy]: # 해당 좌표에서 주변에 해당 좌표의 값보다 크거나 같은 값이 있는지 확인합니다.
                        break # 만약 본인 보다 큰 값이 있다면 브레이크 합니다.
            else: # 브레이크를 한번도 걸지 않았다면 해당 위치가 봉우리 이므로 봉우리 개수를 추가합니다.
                ans += 1
    return ans
Test_Case = int(input())

for test_case in range(Test_Case):
    N = int(input())  # 지도의 크기
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case+1} {how_many_top(N)}')