import sys
from collections import deque
# sys.stdin = open('input.txt')


def computer_virus_num(num, start):
    que = deque([start])
    trace = [0] * (num+1)
    trace[start] = 1

    while que:
        now = que.popleft()
        for next in graph[now]:
            if not trace[next]:
                trace[next] = 1
                que.append(next)
    return sum(trace) - 1

computer_num = int(input())
E = int(input())
graph = [[] for _ in range(computer_num + 1)]
for _ in range(E):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
print(computer_virus_num(computer_num, 1))
