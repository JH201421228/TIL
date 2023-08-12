import sys
from math import gcd
input = sys.stdin.readline

num_of_tree = int(input())
now_tree = [int(input().rstrip()) for _ in range(num_of_tree)]

start_cordinate = now_tree[0]
end_cordinate = now_tree[-1]

between_tree = [now_tree[i + 1] - now_tree[i] for i in range(len(now_tree) - 1)]

gap = min(between_tree)

for i in range(len(between_tree)):
    gap = gcd(gap, between_tree[i])


ans = ((end_cordinate - start_cordinate) // gap) - (len(now_tree) - 1)

print(ans)