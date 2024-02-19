import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


cache = [[0, 0] for _ in range(1_000_001)]

cache[1][0], cache[1][1] = 3, 4

mod = 1_000_000_007

for i in range(1, 1_000_000):
    cache[i+1][0] = (cache[i][0] * 3 + cache[i][1]) % mod
    cache[i+1][1] = (cache[i][0] * 4 + cache[i][1] * 2) % mod

for _ in range(int(input())):
    print(sum(cache[int(input())]) % mod)