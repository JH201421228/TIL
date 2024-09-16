import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100_000)


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])

    return p[x]

def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        p[b] = a
    else:
        p[a] = b


V, E = map(int, input().split())

ans = 0
cnt = 0

w = []

for _ in range(E):
    a, b, c = map(int, input().split())

    heapq.heappush(w, (c, a, b))

p = [i for i in range(V+1)]

while w:
    a, b, c = heapq.heappop(w)

    if find(b) != find(c):
        union(b, c)
        ans += a
        cnt += 1

    if cnt == V-1:
        break

print(ans)