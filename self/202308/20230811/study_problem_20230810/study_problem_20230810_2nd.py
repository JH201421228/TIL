import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def BFS(X, K, N):
    deq = deque([])
    deq.append(X)
    trace = [0] * (N+1)
    trace[X] = 1
    ans = []
    while deq:
        now = deq.popleft()
        for next in range(1, N + 1):
            if not trace[next] and matrix[now][next]:
                trace[next] = trace[now] + 1
                deq.append(next)
                if trace[next] == K + 1:
                    ans.append(next)
                if trace[next] > K + 1:
                    return ans
    return [-1]


N, M, K, X = list(map(int, input().split()))
# matrix = [[0] * (N + 1) for _ in range(N + 1)]
start_info = []
for _ in range(M):
    start, end = map(int, input().split())
    start_info.append(start)

# ans = BFS(X, K, N)
#
# for num in ans:
#     print(num)

