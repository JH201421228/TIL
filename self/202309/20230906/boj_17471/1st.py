import sys
from itertools import combinations
sys.stdin = open('input.txt')

city_num = int(input())
population = list(map(int, input().split()))
city_map = [[] for _ in range(city_num)]
for i in range(city_num):
    info = list(map(int, input().split()))
    for idx in range(1, info[0] + 1):
        city_map[i].append(info[idx] - 1)
print(city_map)