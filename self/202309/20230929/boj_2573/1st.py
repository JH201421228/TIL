import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def count_sea_block():
    sea_block = [0] * (N*M)
    for idx in range(N*M):
        if iceberg[idx//M][idx%M]:
            cnt = 0
            for dx, dy in delta:
                if 0 <= idx//M + dx < N and 0 <= idx%M +dy < M and not iceberg[idx//M + dx][idx%M +dy]:
                    cnt += 1
            sea_block[idx] = cnt
    return sea_block

def why_do_this():
    check_list = [0] * (N*M)
    que = deque([])
    cnt = 0
    for idx in range(N*M):
        if iceberg[idx//M][idx%M] and not check_list[idx]:
            check_list[idx] = 1
            que.append((idx//M, idx%M))
            while que:
                x, y = que.popleft()
                for dx, dy in delta:
                    if 0 <= x+dx < N and 0 <= y+dy < M and iceberg[x+dx][y+dy] and not check_list[(x+dx)*M + y+dy]:
                        check_list[(x + dx) * M + y + dy] = 1
                        que.append((x+dx, y+dy))
            cnt += 1
    return cnt


N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

# 빙산 주위를 둘러싸고 있는 바닷물의 개수를 반환하는 함수 생성
# 루프를 돌며 빙산이 녹는 것을 재현
# 빙산이 녹아 0이 되는 지점이 생기면 빙산이 몇 조각인지 체크
total_year = 0
# print(count_sea_block())
# print(why_do_this())
while True:
    sea_block = count_sea_block()
    while True:
        flag = 0
        cnt_year = 0
        for idx in range(N*M):
            if iceberg[idx//M][idx%M]:
                val = iceberg[idx//M][idx%M] - sea_block[idx]
                if val < 0:
                    val = 0
                    flag = 1
                iceberg[idx // M][idx % M] = val
        cnt_year += 1
        if flag:
            break
    total_year += cnt_year
    cnt = why_do_this()
    if cnt != 1:
        break
if cnt > 1:
    print(total_year)
else:
    print(0)
