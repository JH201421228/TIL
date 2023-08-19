import sys
sys.stdin = open('input.txt')

col_num = int(input())
col_info = [list(map(int, input().split())) for _ in range(col_num)]
col_info.sort()
max_col = 0
for idx, info in enumerate(col_info):
    if max_col < info[1]:
        max_col = info[1]
        max_idx = idx
# print(max_col, max_idx)

acre = 0

if max_idx == col_num - 1: # 가장 큰 기둥이 맨 마지막에 있는 경우
    for i in range(col_num - 1):
        if col_info[i][1] > col_info[i+1][1]: # 앞에 있는 기둥이 더 큰 경우
            acre += col_info[i][1] * (col_info[i+1][1] - col_info[i][1])
elif not max_idx: # 가장 큰 기중이 맨 처음에 있는 경우
    pass
else: # 이도 저도 아닌 경우

# print(col_info)