import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
# from collections import deque


N = int(input())

arr = [[] for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())

    heapq.heappush(arr[a], -b)


hq = []
for idx in range(1, N+1):
    for _ in range(idx):

        if not arr[idx]:
            break
        if len(hq) < idx:
            heapq.heappush(hq, heapq.heappop(arr[idx]))
            hq.sort()
        else:
            if hq[-1] > arr[idx][0]:
                hq.pop()
                heapq.heappush(hq, heapq.heappop(arr[idx]))
                hq.sort()

print(-sum(hq))


