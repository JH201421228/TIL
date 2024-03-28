import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
arr.sort(key=lambda x: -x[0])
# print(arr)
cnt = 0
q = []
while arr:
    a, b = arr.pop()
    if cnt < a:
        heapq.heappush(q, b)
        cnt += 1
    else:
        if q[0] < b:
            heapq.heappop(q)
            heapq.heappush(q, b)
    # print(q)
print(sum(q))
