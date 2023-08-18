import sys
# sys.stdin = open('input.txt')

N = int(input())
tri_list = [list(map(int, input().split())) for _ in range(N)]
plz_solve_this = [[0]*(i+1) for i in range(N)]
plz_solve_this[0][0] = tri_list[0][0]

for i in range(1, N):
    for j in range(i):
        for k in range(2):
            two_sum_num = plz_solve_this[i-1][j] + tri_list[i][j+k]
            if not plz_solve_this[i][j+k]:
                plz_solve_this[i][j+k] = two_sum_num
            elif plz_solve_this[i][j+k] < two_sum_num:
                plz_solve_this[i][j + k] = two_sum_num


print(max(plz_solve_this[-1]))