import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

qx, qy = [], []

for _ in range(N):
    heapq.heappush(qx, tuple(map(int, input().split())))

ans = 0
isFirstTime = True
isOddTurn = True

first = tuple()

pre = 0

while qx:
    x, y = heapq.heappop(qx)
    heapq.heappush(qy, (y, x))

    if isFirstTime:
        first = (x, y)
        isFirstTime = not isFirstTime

    if isOddTurn:
        pre = y
        isOddTurn = not isOddTurn
    else:
        ans += (y - pre)
        isOddTurn = not isOddTurn

isFirstTime = True
isOddTurn = True

first = tuple()

pre = 0

while qy:
    y, x = heapq.heappop(qy)

    if isFirstTime:
        first = (x, y)
        isFirstTime = not isFirstTime

    if isOddTurn:
        pre = x
        isOddTurn = not isOddTurn
    else:
        ans += (x - pre)
        isOddTurn = not isOddTurn

print(ans)