import sys
from itertools import product
# sys.stdin = open('input.txt')
N = int(input())
tri_int = [list(map(int, input().split())) for _ in range(N)]
bin_list = [0, 1]
ans = list(product(bin_list, repeat=N-1))

max_val = 0
for inner_list in ans:
    idx = 0
    total = tri_int[0][0]
    for j in range(1, N):
        idx += inner_list[j-1]
        total += tri_int[j][idx]
    if total > max_val:
        max_val = total
print(max_val)