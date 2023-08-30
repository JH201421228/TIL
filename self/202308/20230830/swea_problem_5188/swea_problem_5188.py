import sys
from collections import deque
sys.stdin = open('input.txt')


def so_tired_now(return_val, N):
    delta = [[1, 0], [0, 1]]
    que = deque([[0, 0]])


    while que:
        x, y = que.popleft()
        if check_graph[N-1][N-1][1] == return_val:
            return check_graph[N-1][N-1]
        for dx, dy in delta:
            if x+dx < N and y+dy < N:
                if not check_graph[x+dx][y+dy][0] or check_graph[x+dx][y+dy][0] > check_graph[x][y][0] + graph[x+dx][y+dy]:
                    check_graph[x+dx][y+dy][0] = check_graph[x][y][0] + graph[x+dx][y+dy]
                    check_graph[x+dx][y+dy][1] = check_graph[x][y][1] + 1
            que.append([x+dx, y+dy])


T = int(input())
for test in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # for inner in graph:
    #     print(inner)
    # print('----------------')
    check_graph = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    check_graph[0][0][0] = graph[0][0]
    # print(check_graph)
    print(f'#{test+1} {so_tired_now(N * 2 - 2, N)[0]}')
    for inner in graph:
        print(inner)
    print('------------------------')
    for inner in check_graph:
        print(inner)
    print()
    # print(check_graph)