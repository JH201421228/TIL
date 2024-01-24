import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(now, cnt):
    visited[now] = 1
    for next in graph[now]:
        if not visited[next]:
            cnt = dfs(next, cnt+1)
    return cnt


for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)
    visited = [0] * (N+1)
    print(dfs(1, 0))