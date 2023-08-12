# 숫자 배열 회전
import sys
sys.stdin = open('input.txt')

def rotation_270(arr, N):
    rotated_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated_arr[i][j] = arr[j][N-i-1]

    return rotated_arr

def rotation_180(arr, N):
    rotated_arr_270 = rotation_270(arr, N)
    return rotation_270(rotated_arr_270, N)

def rotation_90(arr, N):
    rotated_arr_180 = rotation_180(arr, N)
    return  rotation_270(rotated_arr_180, N)

Test_Case = int(input())

for test_case in range(Test_Case):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = rotation_90(arr, N)
    arr_180 = rotation_180(arr, N)
    arr_270 = rotation_270(arr, N)

    print(f'#{test_case + 1}')
    for i in range(N):
        str_90 = [str(i) for i in arr_90[i]]
        str_180 = [str(i) for i in arr_180[i]]
        str_270 = [str(i) for i in arr_270[i]]

        print(''.join(str_90), ''.join(str_180), ''.join(str_270))