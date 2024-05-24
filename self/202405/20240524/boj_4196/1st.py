import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


for _ in range(int(input())):
    N, M = map(int, input().split())
    ing = [0] * (N+1)
    order = [[] for _ in range(N+1)]
    start_point = [True] * (N+1)

    for _ in range(M):
        s, e = map(int, input().split())
        ing[e] += 1
        order[s].append(e)
        start_point[e] = False

    for idx in range(1, N+1):
        if start_point[idx]:
            q = deque([idx])
            while q:
                now = q.popleft()
                for next in order[now]:
