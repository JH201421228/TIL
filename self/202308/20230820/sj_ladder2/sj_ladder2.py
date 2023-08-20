import sys
sys.stdin = open('input.txt')


# 델타 탐색(좌 우 하)
di = [0, 0, 1]
dj = [-1, 1, 0]

for _ in range(10):
    test = int(input())
    Board = [list(map(int, input().split())) for _ in range(100)]
    shortest = 0        # 인덱스
    distance = 100*100  # 거리 난 최소를 구할 것이라 계속 최소로 초기화 하고 싶음
    ni = 0

    # 출발점 탑색
    for j in range(100):
        if Board[ni][j] == 1:
            # j 가 출발점의 j좌표
            nj = j
            visited = [[0]*100 for _ in range(100)]
            move_count = 0
            # 바닥에 도착할 때까지 움직일 것이다.
            while ni != 99:
                for k in range(3):
                    ni += di[k]
                    nj += dj[k]
                    if (0 <= ni < 100) and (0 <= nj < 100) and (Board[ni][nj] == 1) and (visited[ni][nj] == 0):
                        visited[ni][nj] = 1
                        move_count += 1
                        break
                    else:
                        ni -= di[k]
                        nj -= dj[k]
            # 여기까지 사다리는 잘 움직이는데 값 초기화가 안되넹


            # 한 출발점마다 거리 잰 다음에 작으면 그 기준점 초기화하고 인덱스 입력하는건데
            if move_count <= distance:
                distance = move_count
                shortest = j

    print(f'#{test}', shortest)