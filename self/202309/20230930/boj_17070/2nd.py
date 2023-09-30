import sys
sys.stdin = open('input.txt')


delta0 = [(0, 1), (1, 1)] #status 0 -> 0, 2
delta1 = [(1, 0), (1, 1)] #status 1 -> 1, 2
delta2 = [(0, 1), (1, 0), (1, 1)] #status 2 -> 0, 1, 3
delta = [delta0, delta1, delta2]

def holiday(x, y, status):
    if status == 2:
        global ans
        ans += 1
    # for inner in visited:
    #     print(inner)
    # print('-------------')

    if x == y == N-1:
        return 1

    if visited[x][y] >= 0:
        return visited[x][y]

    visited[x][y] = 0

    for dx, dy in delta[status]:
        if 0 <= x+dx < N and 0 <= y+dy < N:
            if not dx*dy:
                if not housing[x+dx][y+dy]:
                    if not dx:
                        visited[x][y] += holiday(x+dx, y+dy, 0)
                    else:
                        visited[x][y] += holiday(x+dx, y+dy, 1)
            else:
                if not housing[x+dx][y+dy] and not housing[x][y+dy] and not housing[x+dx][y]:

                    visited[x][y] += holiday(x+dx, y+dy, 2)
    return visited[x][y]

N = int(input())
housing = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
ans = 0
print(holiday(0, 1, 0))
print(ans)
# for inner in visited:
#     print(inner)