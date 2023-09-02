import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(15000)

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def catch_me_if_you_can(start_x, start_y, now_num):
    global max_num
    if now_num > max_num:
        max_num = now_num
        ans_list.append([now_num, n_by_n[start_x][start_y]])

    for dx, dy in delta:
        if 0 <= start_x+dx < n and 0 <= start_y+dy < n and n_by_n[start_x+dx][start_y+dy] == n_by_n[start_x][start_y] + 1:
            catch_me_if_you_can(start_x+dx, start_y+dy, now_num + 1)

T = int(input())
for test in range(T):
    n = int(input())
    n_by_n = [list(map(int, input().split())) for _ in range(n)]
    max_num = 0
    ans_list = []
    for start_x in range(n):
        for start_y in range(n):
            catch_me_if_you_can(start_x, start_y, 1)

    ans_list.sort()
    for inner in ans_list:
        if inner[0] == max_num:
            print(f'#{test + 1} {inner[1] - inner[0] + 1} {max_num}')
    # print(max_num)
    # print(ans_list)

