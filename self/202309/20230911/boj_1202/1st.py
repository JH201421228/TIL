import sys
import heapq
sys.stdin = open('input.txt')

def thief():



N, K = map(int, input().split())
jew_info = [list(map(int, input().split())) for _ in range(N)]
inventory = list(int(input()) for _ in range(K))
print(jew_info)
print(inventory)

