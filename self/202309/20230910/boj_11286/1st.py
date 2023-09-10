import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


heap = []
N = int(input())
for _ in range(N):
    num = int(input())
    if not num:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))
