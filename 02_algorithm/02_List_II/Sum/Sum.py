import sys
sys.stdin = open('input.txt')

for i in range(10):
    Test_Case = int(input())
    Test_List = []
    for _ in range(100):
        Test_List.append(list(map(int, input().split())))

    Trans_Test_List = [[0]*100 for _ in range(100)]

    for j in range(100):
        for k in range(100):
            Trans_Test_List[j][k] = Test_List[k][j]
    # 메트릭스 2개 정의
    row_max = Test_List[0][0]
    for j in range(100):
        if sum(Test_List[j]) > row_max:
            row_max = sum(Test_List[j])

    col_max = Trans_Test_List[0][0]
    for j in range(100):
        if sum(Trans_Test_List[j]) > col_max:
            col_max = sum(Trans_Test_List[j])

    diagonal1_max = Test_List[0][0]
    for j in range(1, 100):
        diagonal1_max += Test_List[j][j]

    diagonal2_max = Test_List[0][99]
    for j in range(1, 100):
        diagonal2_max += Test_List[j][99-j]

    print(f'#{i+1} {max(row_max, col_max, diagonal1_max, diagonal2_max)}')