import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
# from collections import deque


N = int(input())

arr = []
for _ in range(N):
    deadline, ramen_num = map(int, input().split())
    heapq.heappush(arr, (-ramen_num, deadline))
# print(arr)
visited = dict()
ans = 0
while arr:
    val, num = heapq.heappop(arr)
    # print(heapq.heappop(arr))
    while num > 0:
        if not num in visited:
            visited[num] = 1
            ans += val
            break
        num -= 1
print(-ans)