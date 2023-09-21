import sys
sys.stdin = open('input.txt')


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def i_want_to_solve_this_problem_by_DP(x, y, val):
    global ans

    if x == y == N-1:
        if ans > val:
            ans = val
        return

    if val >= ans:
        return

    for dx, dy in delta:
        if 0 <= x+dx < N and 0 <= y+dy < N:
            if not check_list[x+dx][y+dy]:
                check_list[x+dx][y+dy] = 1
                i_want_to_solve_this_problem_by_DP(x+dx, y+dy, val + matrix[x+dx][y+dy])
                check_list[x+dx][y+dy] = 0


T = int(input())
for test in range(T):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    print(matrix)
    # 상하좌우로 움직임
    # 최소값으로 교체 가능
    # 끝에 도달하면 출력
    check_list = [[0] * N for _ in range(N)]
    check_list[0][0] = 1
    ans = float('inf')
    i_want_to_solve_this_problem_by_DP(0, 0, 0)
    print(ans)
