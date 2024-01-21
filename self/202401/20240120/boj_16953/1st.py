import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(n):

    q = deque([(n, 1)])
    while q:
        now, ans = q.popleft()
        next1 = now * 10 + 1
        next2 = now * 2
        if next1 == B or next2 == B:
            return ans + 1
        if next1 <= B:
            q.append((next1, ans+1))
        if next2 <= B:
            q.append((next2, ans+1))

    return -1

A, B = map(int, input().split())

print(bfs(A))
