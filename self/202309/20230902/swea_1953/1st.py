import sys
sys.stdin = open('input.txt')

tunnel = {1: [[1, 0], [0, 1], [0, -1], [-1, 0]],
          2: [[1, 0], [-1, 0]],
          3: [[0, 1], [0, -1]],
          4: [[-1, 0], [0, 1]],
          5: [[0, 1], [1, 0]],
          6: [[0, -1], [1, 0]],
          7: [[-1, 0], [0, -1]]}

def prison_break(time):
    ans = 1
    que = [[start_x, start_y, time]]
    while que:
        x, y, t = que.pop(0)
        if t == time_limit:
            return ans
        for dx, dy in tunnel[under_ground[x][y]]:
            if 0 <= x+dx < N and 0 <= y+dy < M and under_ground[x+dx][y+dy] and not check_list[x+dx][y+dy]:
                for cx, cy in tunnel[under_ground[x+dx][y+dy]]:
                    if not dx+cx and not dy+cy:
                        check_list[x+dx][y+dy] = 1
                        que.append([x+dx, y+dy, t + 1])
                        ans += 1
    return ans




T = int(input())
for test in range(T):
    N, M, start_x, start_y, time_limit = map(int, input().split())
    under_ground = [list(map(int, input().split())) for _ in range(N)]
    check_list = [[0] * M for _ in range(N)]
    # print(check_list)
    check_list[start_x][start_y] = 1
    print(f'#{test+1} {prison_break(1)}')
