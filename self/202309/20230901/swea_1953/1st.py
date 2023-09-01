import sys
sys.stdin = open('input.txt')

tunnel = {1: [[1, 0], [0, 1], [-1, 0], [0, -1]],
          2: [[1, 0], [-1, 0]],
          3: [[0, 1], [0, -1]],
          4: [[-1, 0], [0, 1]],
          5: [[1, 0], [0, 1]],
          6: [[0, -1], [1, 0]],
          7: [[-1, 0], [0, -1]]}


def prison_break(start_x, start_y, what_time_now):

    ans = 0
    que = [[start_x, start_y, what_time_now]]
    while que:
        x, y, time = que.pop(0)
        if time == limit_time:
            return ans
        for dx, dy in tunnel[under_ground[x][y]]:
            if 0 <= x+dx < N and 0 <= y+dy < M and under_ground[x+dx][y+dy] and not where_are_u_going_now[x+dx][y+dy]:
                for cx, cy in tunnel[under_ground[x+dx][y+dy]]:
                    if not dx+cx and not cy+dy:
                        where_are_u_going_now[x+dx][y+dy] = 1
                        ans += 1
                        que.append([x+dx, y+dy, time + 1])
                        # print(x+dx, y+dy)
                        break
    return ans

T = int(input())
for test in range(T):
    N, M, start_x, start_y, limit_time = map(int, input().split())
    under_ground = [list(map(int, input().split())) for _ in range(N)]
    # print(under_ground)
    where_are_u_going_now = [[0] * M for _ in range(N)]
    where_are_u_going_now[start_x][start_y] = 1
    # prison_break(start_x, start_y, 0)
    ans = 0
    print(f'#{test + 1} {prison_break(start_x, start_y, 1) + 1}')
    # print(ans)
