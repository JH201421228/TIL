import sys
sys.stdin = open('input.txt')

N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
ans = 0
now_cost = 1000000001
for idx in range(N-1):
    if cost[idx] < now_cost:
        now_cost = cost[idx]
    ans += road[idx] * now_cost
print(ans)