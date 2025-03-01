import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

q = []

pre = 0
cur = N
while True:
    power = 1
    while 2**power <= cur:
        power += 1

    square = 2**power
    pre = cur
    n = square - cur

    while n <= pre:
        q.append(n)
        n += 1
        cur -= 1

        if not cur:
            break

    if not cur:
        break

while q:
    print(q.pop())
