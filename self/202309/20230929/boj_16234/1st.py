import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday():
    que = deque([])
    checker_list = [0] * (N**2)
    return_list = []

    for idx in range(N**2):
        if not checker_list[idx]:
            checker_list[idx] = 1
            temp_list = [(idx//N, idx%N)]
            value = country[idx//N][idx%N]
            que.append((idx//N, idx%N, value))
            while que:
                x, y, val = que.popleft()
                for dx, dy in delta:
                    if 0 <= x+dx < N and 0 <= y+dy < N and not checker_list[(x+dx)*N + y+dy] and L <= abs(val - country[x+dx][y+dy]) <= R:
                        checker_list[(x+dx)*N + y+dy] = 1
                        temp_list.append((x+dx, y+dy))
                        next_val = country[x+dx][y+dy]
                        value += next_val
                        que.append((x+dx, y+dy, next_val))
            if len(temp_list) > 1:
                return_list.append((temp_list, value))

    if return_list:
        return return_list
    else:
        return False


N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    return_list = holiday()
    if return_list:
        ans += 1
        for temp_list, value in return_list:
            val = value//len(temp_list)
            for x, y in temp_list:
                country[x][y] = val
    else:
        break

print(ans)
# print(country)
# bfs 를 돌면서 연결 가능한 숫자들을 연결
