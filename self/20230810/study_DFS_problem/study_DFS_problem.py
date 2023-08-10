import sys
sys.stdin = open('input.txt')


def DFS(start, N, K):
    trace = [0] * (N+1)
    trace[start] = 1
    stack = [start]
    ans = 0
    while stack:
        now = stack.pop()
        for next in range(1, N+1):
            if not trace[next] and matrix[now][next]:
                trace[next] = 1
                stack.append(next)
                if


N, M, K, X = map(int, input().split()) # N = 도시의 개수, M = 도로의 개수, K = 거리 정보, X = 출발 도시

matrix = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    matrix[start][end] = 1

print(matrix)