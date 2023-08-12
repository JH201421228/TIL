import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline

def DFS(V):
    path[V] = 1
    for next in graph[V]:
        if not path[next]:
            ans.append(next)
            DFS(next)
    return ans

def BFS(N, V): # 수정 필요
    stack = deque([])
    stack.append(V)
    ans2 = [V]
    trace = [0] * (N + 1)
    trace[V] = 1
    while stack:
        start = stack.popleft()
        for next in graph[start]:
            if not trace[next]:
                stack.append(next)
                trace[next] = 1
                ans2.append(next)
    return ans2




N, M, V = map(int, input().split()) # N : vertax, M : edge, V : start_num
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
path = [0] * (N + 1)
ans = [V]
mapping = []
for inner_list in graph:
    inner_list.sort()
    mapping.append(inner_list)
# print(graph)
# print(mapping)
print(*DFS(V))
print(*BFS(N, V))


