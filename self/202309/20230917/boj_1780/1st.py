import sys
sys.stdin = open('input.txt')


def problem_1780(x1, x2, y1, y2):
    if x1 == x2 or y1 == y2:
        ans_list[paper[x1][y1]] += 1
        return

    if x1 > x2 or y1 > y2:
        return

    for i in range(x1, x2):
        flag = 0
        for j in range(y1, y2):
            check_num = paper[x1][y1]
            if paper[i][j] != check_num:
                flag = 1
                break
        if flag:
            problem_1780(x1, x1 + (x2 - x1) // 3, y1, y1 + (y2 - y1) // 3)
            problem_1780(x1, x1 + (x2 - x1) // 3, y1 + (y2 - y1) // 3, y1 + ((y2 - y1) // 3) * 2)
            problem_1780(x1, x1 + (x2 - x1) // 3, y1 + ((y2 - y1) // 3) * 2, y2)

            problem_1780(x1 + (x2 - x1) // 3, x1 + ((x2 - x1) // 3) * 2, y1, y1 + (y2 - y1) // 3)
            problem_1780(x1 + (x2 - x1) // 3, x1 + ((x2 - x1) // 3) * 2, y1 + (y2 - y1) // 3, y1 + ((y2 - y1) // 3) * 2)
            problem_1780(x1 + (x2 - x1) // 3, x1 + ((x2 - x1) // 3) * 2, y1 + ((y2 - y1) // 3) * 2, y2)

            problem_1780(x1 + ((x2 - x1) // 3) * 2, x2, y1, y1 + (y2 - y1) // 3)
            problem_1780(x1 + ((x2 - x1) // 3) * 2, x2, y1 + (y2 - y1) // 3, y1 + ((y2 - y1) // 3) * 2)
            problem_1780(x1 + ((x2 - x1) // 3) * 2, x2, y1 + ((y2 - y1) // 3) * 2, y2)

            break
    else:
        ans_list[check_num] += 1




N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# print(paper)
ans_list = [0] * 3
problem_1780(0, N, 0, N)
print(ans_list[-1])
print(ans_list[0])
print(ans_list[1])