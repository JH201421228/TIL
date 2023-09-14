import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = list(map(int, input().split()))
check_list = [1] * N

for i in range(1, N):
    temp = []
    for j in range(i):
        if num_list[i] > num_list[j]:
            temp.append(check_list[j])
    if temp:
        check_list[i] = max(temp) + 1
print(max(check_list))