import sys
sys.stdin = open('input.txt')


def DFS(start):
    graph[start].sort(reverse=True)
    trace[start] = 1
    for next in graph[start]:
        if not trace[next]:
            DFS(next)
    return trace


V, E, start = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    p1, p2 = map(int, input().split())
    graph[p1].append(p1)
    graph[p2].append(p2)
trace = [0] * (V+1)
print(DFS(start))