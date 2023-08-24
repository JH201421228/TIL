import sys
sys.stdin = open('input.txt')

horizon, vertical = map(int, input().split())
N = int(input())
cut_info = [list(map(int, input().split())) for _ in range(N)]
# 가로 컷 0, 세로 컷 1
horizon_list = [0] * (vertical + 1)
vertical_list = [0] * (horizon + 1)
horizon_list[-1] = 1
vertical_list[-1] = 1
for x, idx in cut_info:
    if x:
        vertical_list[idx] = 1
    else:
        horizon_list[idx] = 1
v = []
h = []

cnt = 0
for i in vertical_list:
    if i:
        v.append(cnt)
        cnt = 0
    cnt += 1

cnt = 0
for i in horizon_list:
    if i:
        h.append(cnt)
        cnt = 0
    cnt += 1
area = 0
for x in h:
    for y in v:
        if x*y > area:
            area = x*y
print(area)