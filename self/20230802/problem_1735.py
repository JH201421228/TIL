import sys
input = sys.stdin.readline

son1, mom1 = map(int, input().split())
son2, mom2 = map(int, input().split())

son = (son1 * mom2) + (son2 * mom1)
mom = mom1 * mom2

min_val = min(son, mom)

for num in range(min_val, 0, -1):
    if son % num == 0 and mom % num == 0:
        print(son // num, mom // num)
        break