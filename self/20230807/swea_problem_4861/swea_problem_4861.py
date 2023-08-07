import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

def is_pal(arr, N):
    for N



for test_case in range(Test_Case):
    N, M = map(int, input().split())

    str_matrix = [list(input()) for _ in range(N)]

    trans_str_matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            trans_str_matrix[i][j] = str_matrix[j][i]

    for inner_str in str_matrix:
