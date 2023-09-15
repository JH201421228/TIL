import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
ans_list = num_list[:]

for idx in range(1, N):
    ans_list[idx] += ans_list[idx-1]
# print(ans_list)
# print(num_list)
for _ in range(M):
    start_idx, end_idx = map(int, input().split())
    print(ans_list[end_idx-1] - ans_list[start_idx-1] + num_list[start_idx-1])