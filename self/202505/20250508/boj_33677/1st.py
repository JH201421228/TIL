import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    q = deque([1])
    V = [0] * (N+1)

    while q:
        n = q.popleft()

        if N+1 > n+1 and days[n+1] >= days[n]+1:
            days[n+1] = days[n]+1
            q.append(n+1)
            if water[n+1] > water[n]+1:
                water[n+1] = water[n]+1
        if N+1 > n*3 and days[n*3] > days[n]+1:
            days[n*3] = days[n]+1
            q.append(n*3)
            if water[n*3] > water[n]+3:
                water[n*3] = water[n]+3
        if N+1 > n**2 and days[n**2] > days[n]+1:
            days[n**2] = days[n]+1
            q.append(n**2)
            if water[n**2] > water[n]+5:
                water[n**2] = water[n]+5


N = int(input())

if N:
    days = [float("inf")] * (N + 1)
    days[1] = 1
    water = [float("inf")] * (N + 1)
    water[1] = 1
    bfs()
    print(days[-1], water[-1])
else:
    print(0, 0)