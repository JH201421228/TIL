import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


while True:
    N = int(input())
    if not N:
        break
    maze = [[] for _ in range(N+1)]
    cost = [0] * (N+1)
    for i in range(N):
        temp = list(input().split())
        if temp[0] == 'L':
            cost[i+1] = int(temp[1])
        elif temp[0] == 'T':
            cost[i+1] = -int(temp[1])
        j = 2
        while True:
            if temp[j] == '0':
                break
            maze[i+1].append(int(temp[j]))
            j += 1
    # print(maze)
    # print(cost)
    cost_now = 0
    visited = [-1] * (N+1)
    q = deque([1])
    visited[1] = 0

    while q:
        now = q.popleft()
        for next in maze[now]:
            if visited[next] < cost_now:
                if not cost[next]:
                    visited[next] = cost_now
                    q.append(next)
                elif cost[next] > 0:
                    cost_now = max(cost_now, cost[next])
                    visited[next] = cost_now
                    q.append(next)
                else:
                    if cost_now + cost[next] >= 0:
                        cost_now = cost_now + cost[next]
                        visited[next] = cost_now
                        q.append(next)
    if visited[-1] != -1:
        print('Yes')
    else:
        print('No')