

Test = int(input()) # 전체 테스트 케이스의 횟수를 받습니다.

for test in range(Test): # 테스트 케이스 횟수만큼 반복합니다.
    N = int(input()) # 풍선이 들어있는 정방형 메트릭스의 크기를 받습니다.
    ballon = [list(map(int, input().split())) for _ in range(N)] # 풍선의 정보를 2차원 배열로 받습니다.

    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 델타 탐색 범위를 지정합니다.
    max_val = 0 # 최대값으로 쓰일 변수를 선언합니다.
    min_val = 20*20*9 # 최소값으로 쓰일 변수를 선언합니다.
    for i in range(N): # 풍선 정보가 든 2차원 배열을 순회합니다.
        for j in range(N):
            total = ballon[i][j] # 초기값에 풍선을 터트리기 시작할 풍선 값을 넣습니다.
            for di, dj in delta: # 델타 값을 받아옵니다.
                for x in range(1, ballon[i][j] + 1): # 처음 터트린 풍선에 든 값의 크기만큼 델타 탐색을 하겠습니다.
                    if 0 <= i+di*x < N and 0 <= j+dj*x < N: # 해당 좌표들이 2차원 배열 안에 있다면
                        total += ballon[i+di*x][j+dj*x] # 해당 좌표에 있는 풍선이 가진 값을 더해주겠습니다.
            if total > max_val: # 최대값과 최솟값을 수정합니다.
                max_val = total
            if total < min_val:
                min_val = total
    print(f'#{test+1} {max_val-min_val}') # 최대값과 최소값의 차이를 출력합니다.