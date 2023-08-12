import sys
sys.stdin = open('input.txt')


def is_pal(arr):
    N = len(arr)
    for index in range(N//2):
        if arr[index] != arr[N-1-index]:
            return False

    return True
# 여기까지 회문 판별기 정의


def pal_counter(arr, N): # N 찾아야 하는 회문 길이
    M = 8 # 메트릭스 길이
    count = 0
    for i in range(M-N+1):
        if is_pal(arr[i:i+N]):
            count += 1

    return count


for test_case in range(10):
    N = int(input())
    matrix = [list(input()) for _ in range(8)]
    trans_matrix = [[0] * 8 for _ in range(8)]

    for i in range(8):
        for j in range(8):
            trans_matrix[i][j] = matrix[j][i]

    # 메트릭스 입력받기 및 전위 메트릭스 생성 완료
    total = 0
    for arr in matrix:
        total += pal_counter(arr, N)

    for arr in trans_matrix:
        total += pal_counter(arr, N)

    print(f'#{test_case + 1} {total}')
