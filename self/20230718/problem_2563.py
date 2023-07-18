
matrix = [[0] * 100 for _ in range(100)] #100x100 메트릭스 생성
test_case = int(input())
total_list = []

for test_num in range(test_case):
    x, y = map(int, input().split()) #종이를 붙일 주소 할당

    for i in range(x - 1, x + 9):

        for j in range(y - 1, y + 9):
            matrix[j][i] = 1

for _ in range(100):
    total_list.append(sum(matrix[_]))

print(sum(total_list))
# print(total_list)
# for i in range(100):
#     print(matrix[i])