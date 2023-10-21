import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# R 1, G 2, B 3, P 4, Y 5 ???
# 전체를 순회
# '.'이 아닌 문자를 만나면 bfs 시작
# 같은 문자를 4개 이상 만나면 puyo 배열 변환


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(char, que):
    q = deque([que])
    visited[que[0]][que[1]] = 1
    cnt = 1
    temp = [que]
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < 12 and 0 <= y+dy < 6 and puyo[x+dx][y+dy] == char and not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = 1
                cnt += 1
                temp.append((x+dx, y+dy))
                q.append((x+dx, y+dy))
    if cnt >= 4:
        for i, j in temp:
            puyo[i][j] = '.'
        return True
    else:
        for i, j in temp:
            visited[i][j] = 0
        return False


puyo = [list(input().rstrip()) for _ in range(12)]
# print(puyo)

ans = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    flag = 0
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.' and not visited[i][j]:
                if bfs(puyo[i][j], (i, j)):
                    flag = 1
    if flag:
        ans += 1
    else:
        break

    # for inner in puyo:
    #     print(inner)
    # print('------------------')

    for i in range(6):
        temp = []
        for j in range(11, -1, -1):
            if puyo[j][i] != '.':
                temp.append(puyo[j][i])
                puyo[j][i] = '.'
        if temp:
            idx = 12
            for char in temp:
                idx -= 1
                puyo[idx][i] = char

    # for inner in puyo:
    #     print(inner)
    # print('--------------')

    # for inner in visited:
    #     print(inner)

print(ans)

