import sys
from collections import deque
# sys.stdin = open('input.txt')


def Bi_checker(start):
    que = deque([])
    que.append(start)

    if not trace[start]:
        trace[start] = 1

    while que:
        now = que.popleft()
        color = trace[now]
        for next in graph[now]:
            if not trace[next]:
                que.append(next)
                if trace[now] == 1:
                    trace[next] = 2
                elif trace[now] == 2:
                    trace[next] = 1
            if trace[next]:
                if trace[next] == color:
                    return False
    return True


Test_Case = int(input())

for _ in range(Test_Case):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        point1, point2 = map(int, input().split())

        graph[point1].append(point2)
        graph[point2].append(point1)
    trace = [0] * (V+1)

    for start in range(1, V+1):
        if not trace[start]:
            if not Bi_checker(start):
                print('NO')
                break
    else:
        print('YES')
