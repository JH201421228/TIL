def check_func(input_list):
    test_case1 = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
    test_case2 = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
    change_num1 = 0
    change_num2 = 0

    for i in range(8):
        for j in range(8):
            if input_list[i][j] != test_case1[i][j]:
                change_num1 += 1

    for i in range(8):
        for j in range(8):
            if input_list[i][j] != test_case2[i][j]:
                change_num2 += 1

    return min(change_num1, change_num2)

N, M = map(int, input().split())

board_list = []

for i in range(N):
    row = str(input())
    board_list.append(row)
# 여기까지 전체 리스트를 입력 받음


ans = 64
for k in range(N-7):
    for i in range(M-7):
        test_list = []
        for j in range(k, k+8):
            test_list.append(board_list[j][i:i+8])

        if check_func(test_list) < ans:
            ans = check_func(test_list)

print(ans)
# print(check_func(board_list))
# print(board_list) # 출력 테스트용