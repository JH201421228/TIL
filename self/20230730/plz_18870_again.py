import sys

N = int(input())
old_num_list = list(map(int, sys.stdin.readline().split()))

new_num_list = []
for i, num in enumerate(old_num_list):
    new_num_list.append([num, i])

new_num_list.sort()

ans_list = [0] * N  # 초기에 모든 요소를 0으로 채워둠

for i in range(1, N):
    if new_num_list[i][0] == new_num_list[i-1][0]:
        ans_list[new_num_list[i][1]] = ans_list[new_num_list[i-1][1]]
    else:
        ans_list[new_num_list[i][1]] = ans_list[new_num_list[i-1][1]] + 1

# 리스트 출력을 공백으로 구분하여 한 줄에 출력
print(' '.join(map(str, ans_list)))
