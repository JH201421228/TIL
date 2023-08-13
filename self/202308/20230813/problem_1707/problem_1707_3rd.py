import sys
from collections import deque
# sys.stdin = open('input.txt')


def bi_checker(start):
    que = deque([start])
    if not trace[start]:
        trace[start] = 1

    while que:
        now = que.popleft()
        num = trace[now]
        for next in graph[now]:
            if not trace[next]:
                que.append(next)
                if num == 1:
                    trace[next] = 2
                else:
                    trace[next] = 1
            else:
                if trace[next] == num:
                    return False
    return True



Test_Case = int(input())
for _ in range(Test_Case):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    trace = [0] * (V+1)
    for start in range(1, V+1):
        if not trace[start]:
            if not bi_checker(start):
                print('NO')
                break
    else:
        print('YES')
