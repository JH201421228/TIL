import sys
sys.stdin = open('input.txt')

delta = [[-1, 1], [-1, -1], [1, -1], [1, 1]]

total_j, total_i = map(int, input().split())
start_j, start_i = map(int, input().split())
start_i = total_i - start_i
# print(start_i, start_j)
time = int(input())
now_time = 1
delta_idx = 0
now_i = start_i
now_j = start_j

for _ in range(time):

    # if 0 <= now_i + di <= total_i and 0 <= now_j + dj <= total_j and not matrix[now_i + di][now_j + dj]
    if now_i == 0 and now_j == 0:
        delta_idx = 3
    elif now_i == total_i and now_j == 0:
        delta_idx = 0
    elif now_i == 0 and now_j == total_j:
        delta_idx = 2
    elif now_i == total_i and now_j == total_j:
        delta_idx = 1
    elif now_i == 0:
        if [di, dj] == delta[0]:
            delta_idx = 3
        else:
            delta_idx = 2
    elif now_i == total_i:
        if [di, dj] == delta[3]:
            delta_idx = 0
        else:
            delta_idx = 1
    elif now_j == total_j:
        if [di, dj] == delta[3]:
            delta_idx = 2
        else:
            delta_idx = 1
    elif now_j == 0:
        if [di, dj] == delta[1]:
            delta_idx = 0
        else:
            delta_idx = 3
    di, dj = delta[delta_idx]
    now_time += 1
    now_i += di
    now_j += dj
print(now_j, total_i - now_i)