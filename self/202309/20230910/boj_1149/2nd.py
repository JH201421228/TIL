import sys
sys.stdin = open('input.txt')

N = int(input())
cost_list = [list(map(int, input().split())) for _ in range(N)]
# print(cost_list)
for idx in range(1, N):
    cost_list[idx][0] = cost_list[idx][0] + min(cost_list[idx - 1][1], cost_list[idx - 1][2])
    cost_list[idx][1] = cost_list[idx][1] + min(cost_list[idx - 1][0], cost_list[idx - 1][2])
    cost_list[idx][2] = cost_list[idx][2] + min(cost_list[idx - 1][0], cost_list[idx - 1][1])
print(min(cost_list[N-1]))
# print(cost_list)