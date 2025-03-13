import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve(l, r, s, d):
    if r < s:
        return 0

    if l >= s:
        return ((r-s) // d + 1) - math.ceil((l-s) / d)
    else:
        return (r-s) // d + 1


L, R, K = int(input()), int(input()), int(input())

if K == 2:
    print(solve(L, R, 3, 1))
elif K == 3:
    print(solve(L, R, 6, 3))
elif K == 4:
    if L <= 12 and R >= 12:
        print(solve(L, R, 10, 2) - 1)
    else:
        print(solve(L, R, 10, 2))
else:
    print(solve(L, R, 15, 5))