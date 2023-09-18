import sys
sys.stdin = open('input.txt')


def problem_1992(x1, x2, y1, y2):
    if x1 == x2 or y1 == y2:
        ans_list.append('(')
        ans_list.append(matrix[x1][y1])
        ans_list.append(')')
        return
    if x1 > x2 or y1 > y2:
        return

    check_num = matrix[x1][y1]
    for i in range(x1, x2):
        flag = 0
        for j in range(y1, y2):
            if matrix[i][j] != check_num:
                flag = 1
                break
        if flag:
            ans_list.append('(')
            problem_1992(x1, x1 + (x2 - x1) // 2, y1, y1 + (y2 - y1) // 2)
            problem_1992(x1, x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2, y2)
            problem_1992(x1 + (x2 - x1) // 2, x2, y1, y1 + (y2 - y1) // 2)
            problem_1992(x1 + (x2 - x1) // 2, x2, y1 + (y2 - y1) // 2, y2)
            ans_list.append(')')
            break
    else:
        ans_list.append(check_num)
        return


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
# print(matrix)

ans_list = []
problem_1992(0, N, 0, N)
# print(ans_list)
ans = ''
for char in ans_list:
    if type(char) == str:
        ans += char
    else:
        ans += str(char)
print(ans)