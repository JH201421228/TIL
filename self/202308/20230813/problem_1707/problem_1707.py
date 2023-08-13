import sys
from collections import deque
# sys.stdin = open('input.txt')


def Bipartite_checker(V, start):
    trace = [0] * (V+1)
    trace[start] = 1
    que = deque([])
    que.append(start)
    ans = [start]

    while que:
        now = que.popleft()
        for next in graph[now]:
            if not trace[next]:
                if trace[now] == 1:
                    trace[next] = 2
                elif trace[now] == 2:
                    trace[next] = 1
                que.append(next)
                ans.append(next)

    checker = [0] * (V+1)
    checker[start] = 1
    que.append(start)

    length = len(graph)

    for start in range(1, length):
        if graph[start]:
            for next in graph[start]:
                if trace[start] == trace[next]:
                    return 'No'

    for num in trace[1:]:
        if not num:
            return 'No'

    return 'Yes'

Test_Case = int(input())

for _ in range(Test_Case):

    V, E = map(int, input().split())
    if not E:
        print('No')
        continue
    elif V == 1:
        print('Yes')
        continue
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        point1, point2 = map(int, input().split())
        graph[point1].append(point2)
        graph[point2].append(point1)
    start = point1
    print(Bipartite_checker(V, start))