import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def prison_break(start_x, start_y):
    que = deque([(start_x, start_y)])
    visited = [[0] * (w+2) for _ in range(h+2)]
    visited[start_x][start_y] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < h+2 and 0 <= y+dy < w+2 and not visited[x+dx][y+dy]:
                if graph[x+dx][y+dy] == '.' or graph[x+dx][y+dy] == '$':
                    visited[x+dx][y+dy] = visited[x][y]
                    que.appendleft((x+dx, y+dy))
                elif graph[x+dx][y+dy] == '#':
                    visited[x + dx][y + dy] = visited[x][y] + 1
                    que.append((x+dx, y+dy))
    return visited


T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    graph = ['.' * (w + 2)]
    for _ in range(h):
        input_str = input().rstrip()
        graph.append('.' + input_str + '.')
    graph.append('.' * (w + 2))
    prisoner = []
    for i in range(h+2):
        for j in range(w+2):
            if graph[i][j] == '$':
                prisoner.append((i, j))

    # print(prison_break(*prisoner[0]))
    jail1 = prison_break(*prisoner[0])
    jail2 = prison_break(*prisoner[1])
    savior = prison_break(0, 0)
    # for inner in jail1:
    #     print(inner)
    # print('----------------------------------')
    # for inner in jail2:
    #     print(inner)
    # print('----------------------------------')
    # for inner in savior:
    #     print(inner)
    ans = float('inf')
    # for i in range(h+2):
    #     for j in range(w+2):
    #         if graph[i][j] == '#':
    #             ans.append(jail1[i][j] + jail2[i][j] + savior[i][j])
    # print(ans)
    # print(min(ans) - 5)
    # print(jail1[0][0] + jail2[0][0] + savior[0][0])

    for i in range(h+2):
        for j in range(w+2):
                if graph[i][j] == '#':
                    sum_val = jail1[i][j] + jail2[i][j] + savior[i][j] - 2
                    ans = min(sum_val, ans)
    ans = min(ans, jail1[0][0] + jail2[0][0] + savior[0][0])
    print(ans-3)

