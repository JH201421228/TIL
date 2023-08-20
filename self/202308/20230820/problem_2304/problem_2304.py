import sys
sys.stdin = open('input.txt')

col_num = int(input())
col_info = [list(map(int, input().split())) for _ in range(col_num)]
col_info.sort()
col_height = []
max_col = 0
max_idx = 0
for idx, info in enumerate(col_info):
    col_height.append(info[1])
    if info[1] > max_col:
        max_col = info[1]
        max_idx = idx
# 여기까지 받은 값들 정리

if not max_idx: # 최대 기둥이 맨 앞에 있을 때
    now_col = 0
    acer = 0
    for i in range(1, col_num):
        now_col = max(col_height[i:])
        acer += now_col * (col_info[i][0] - col_info[i - 1][0])
    acer += max_col
elif max_idx == col_num - 1: # 최대 기둥이 맨 뒤에 있을 때
    now_col = 0
    acer = 0
    for i in range(col_num - 1):
        if col_info[i][1] > now_col:
            now_col = col_info[i][1]
        acer += now_col * (col_info[i + 1][0] - col_info[i][0])
    acer += max_col
else:
    now_col = 0
    acer = 0
    for i in range(max_idx):
        if col_info[i][1] > now_col:
            now_col = col_info[i][1]
        acer += now_col * (col_info[i+1][0] - col_info[i][0])
    for i in range(max_idx + 1, col_num):
        now_col = max(col_height[i:])
        acer += now_col * (col_info[i][0] - col_info[i-1][0])
    acer += max_col


# print(col_info)
# print(col_height)
# print(max_idx, max_col)
print(acer)