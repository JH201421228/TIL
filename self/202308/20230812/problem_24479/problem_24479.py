import sys
from collections import deque
sys.setrecursionlimit(150000)
# sys.stdin = open('input.txt')


def DFS(R):
    global cnt
    matrix[R].sort()
    trace[R] = cnt
    for next in matrix[R]:
        if not trace[next]:
            cnt += 1
            trace[next] = cnt
            DFS(next)
    return trace

N, M, R = map(int, input().split())
matrix = [[] for _ in range(N+1)]
for _ in range(M):
    point1, point2 = map(int, input().split())
    matrix[point1].append(point2)
    matrix[point2].append(point1)
trace = [0] * (N+1)
cnt = 1
ans = DFS(R)

for i in range(1, N+1):
    print(ans[i])