import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def is_connected(a, b):
    if visited[a][b]:
        return True

    for x in range(V):
        if not v[x] and visited[a][x]:
            v[x] = 1
            if is_connected(x, b):
                return True
            else:
                v[x] = 0

    return False


V, E = map(int, input().split())
ans = 0
cnt = E

visited = [[0] * V for _ in range(V)]
weight = []

for _ in range(E):
    a, b, c = map(int, input().split())
    visited[a-1][b-1], visited[b-1][a-1] = 1, 1
    ans += c
    heapq.heappush(weight, (-c, a-1, b-1))

print(weight)

while cnt > V-1:
    a, b, c = heapq.heappop(weight)
    print(a, b, c)
    visited[b][c], visited[c][b] = 0, 0
    v = [0] * V
    v[b] = 1

    if is_connected(b, c):
        ans += a
        cnt -= 1
    else:
        visited[b][c], visited[c][b] = 1, 1

print(ans)