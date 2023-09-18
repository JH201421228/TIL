import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(15000)


def this_problem_suck(x1, x2, y1, y2):

    if x1 > x2 or y1 > y2 or x2 - x1 != y2 - y1:
        return
    if x1 == x2 and y1 == y2:
        ans_list[paper[x1][x2]] += 1
        return

    check = paper[x1][y1]
    for i in range(x1, x2):
        flag = 0
        for j in range(y1, y2):
            if paper[i][j] != check:
                flag = 1
                break
        if flag:
            this_problem_suck(x1, x1 + (x2 - x1) // 2, y1, y1 + (y2 - y1) // 2)
            this_problem_suck(x1 + (x2 - x1) // 2, x2, y1, y1 + (y2 - y1) // 2)
            this_problem_suck(x1, x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2, y2)
            this_problem_suck(x1 + (x2 - x1) // 2, x2, y1 + (y2 - y1) // 2, y2)
            break

    else:
        ans_list[check] += 1
        return




N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# print(paper)
ans_list = [0, 0]
this_problem_suck(0, N, 0, N)
for num in ans_list:
    print(num)