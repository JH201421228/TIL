# import sys
from collections import deque
# sys.stdin = open('input.txt')


def path_finder(start, end):
    que = deque([start])
    trace[start] = 1

    while que:
        now = que.popleft()
        for next in range(1, V+1):
            if not trace[next] and matrix[now][next]:
                if next == end:
                    return trace[now]
                trace[next] = trace[now] + 1
                que.append(next)
    return 0


Test = int(input())
for test in range(Test):
    V, E = map(int, input().split())
    matrix = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        p1, p2 = map(int, input().split())
        matrix[p1][p2] = 1
        matrix[p2][p1] = 1
    start, end = map(int, input().split())
    trace = [0] * (V+1)
    print(f'#{test + 1} {path_finder(start, end)}')