import sys
sys.stdin = open('input.txt')

N = int(input())
stair_info = [int(input()) for _ in range(N)]
# print(stair_info)

point_list = [[stair_info[0], 0]]
for idx in range(1, N):
    if idx == 1:
        a = stair_info[idx]
    else:
        a = max(point_list[idx - 2]) + stair_info[idx]
    b = stair_info[idx] + point_list[idx - 1][0]

    if point_list[idx - 1][1]:
        c = point_list[idx - 1][1] + stair_info[idx]
    else:
        c = 0

    point_list.append([a, b])
print(max(point_list[-1]))
