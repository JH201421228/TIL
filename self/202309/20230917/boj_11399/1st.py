import sys
sys.stdin = open('input.txt')

N = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
# print(time_list)
for idx in range(N):
    if idx:
        time_list[idx] += time_list[idx-1]
print(sum(time_list))