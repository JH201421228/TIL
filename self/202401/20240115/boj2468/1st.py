import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(i, j):

    que = deque([0, 0])
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    # 처음에 0 0 이면 수정
    check_list = []
    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and area[x+dx][y+dy]:
                check_list.append((x+dx, y+dy))



    return


N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]

check_num = float('inf')

for i in range(N):
    for j in range(N):
        check_num = min(check_num, area[i][j])



# print(check_num)

