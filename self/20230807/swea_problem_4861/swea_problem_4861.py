import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

def is_pal(arr, N):
    for i in range(N//2):
        if arr[i] != arr[N-1-i]:
            return False

    return True



for test_case in range(Test_Case):
    N, M = map(int, input().split())

    str_matrix = [list(input()) for _ in range(N)]

    trans_str_matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            trans_str_matrix[i][j] = str_matrix[j][i]

    print(f'#{test_case + 1}', end=' ')

    for plz_check in str_matrix:
        for index in range(N-M+1):
            inner_str = plz_check[index:index+M+1]
            if is_pal(inner_str, M):
                print(''.join(inner_str))
                break

    for plz_check in trans_str_matrix:
        for index in range(N-M+1):
            inner_str = plz_check[index:index+M+1]
            if is_pal(inner_str, M):
                print(''.join(inner_str))
                break