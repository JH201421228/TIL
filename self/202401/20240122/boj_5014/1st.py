import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs():

    q = deque([S])
    while q:
        now = q.popleft()
        for move in delta:
            if now + move == G:
                return visited[now]
            if 0 < now + move <= F and not visited[now+move]:
                visited[now+move] = visited[now] + 1
                q.append(now + move)

    return "use the stairs"


F, S, G, U, D = map(int, input().split())

delta = [U, -D]

visited = [0] * (F+1)
visited[0] = visited[S] = 1
print(bfs())
