import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def BFS(X, K, N):
    deq = deque([])
    deq.append(X)
    trace = [0] * (N+1)
    trace[X] = 1
    ans = []
    while deq:
        now = deq.popleft()
        for next in matrix[now]: # plz
            if not trace[next]:
                trace[next] = trace[now] + 1
                deq.append(next)
                if trace[next] == K + 1:
                    ans.append(next)

    return ans


N, M, K, X = list(map(int, input().split()))
matrix = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    matrix[start].append(end)

ans = BFS(X, K, N)
ans.sort()
if ans:
    for num in ans:
        print(num)
else:
    print(-1)

