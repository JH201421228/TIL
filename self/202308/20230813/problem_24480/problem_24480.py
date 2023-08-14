import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(150000)


def DFS(now):
    global cnt
    graph[now].sort(reverse=True)
    trace[now] = cnt
    for next in graph[now]:
        if not trace[next]:
            cnt += 1
            DFS(next)
    return trace


V, E, start = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
trace = [0] * (V+1)
cnt = 1
ans = DFS(start)
for i in range(1, len(ans)):
    print(ans[i])