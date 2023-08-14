import sys
from math import gcd

input = sys.stdin.readline

num_of_tree = int(input())
now_tree = [int(input().rstrip()) for _ in range(num_of_tree)]

start_cordinate = now_tree[0]
end_cordinate = now_tree[-1]

between_tree = [now_tree[i + 1] - now_tree[i] for i in range(len(now_tree) - 1)]
short_length_between_tree = min(between_tree)

# 인접한 나무 사이의 차이의 최대공약수(GCD)를 계산합니다.
gap = short_length_between_tree
for i in range(len(between_tree)):
    gap = gcd(gap, between_tree[i])

# 이상적인 나무 시퀀스에 추가해야 할 나무의 개수를 계산합니다.
num_trees_to_add = (end_cordinate - start_cordinate) // gap - (len(now_tree) - 1)

print(num_trees_to_add)
