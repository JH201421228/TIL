import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

for idx in range(len(num_list)):
    if idx:
        num_list[idx] += num_list[idx-1]

# print(num_list)

remain_list = [0] * M

for num in num_list:
    remain_list[num % M] += 1

ans = remain_list[0]

for num in remain_list:
    ans += (num * (num-1)) // 2
print(ans)