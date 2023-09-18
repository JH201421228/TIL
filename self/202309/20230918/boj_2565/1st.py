import sys
sys.stdin = open('input.txt')

N = int(input())
info_list = [list(map(int, input().split())) for _ in range(N)]
info_list.sort()
# print(info_list)
check_list = [1] * 500
# length = len(info_list)
for i in range(1, N):
    temp = []
    for j in range(i):
        if info_list[i][1] > info_list[j][1]:
            temp.append(check_list[j])
    if temp:
        check_list[i] = max(temp) + 1
print(check_list)
print(N - max(check_list))