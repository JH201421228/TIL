import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
order = [[] for _ in range(N+1)]
ing = [0] * (N+1)
ans = [1] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    ing[e] += 1
    order[s].append(e)

q = deque([])
for idx in range(1, N+1):
    if not ing[idx]:
        q.append(idx)

while q:
    now = q.popleft()
    for next in order[now]:
        ans[next] = max(ans[next], ans[now] + 1)
        ing[next] -= 1
        if not ing[next]:
            q.append(next)

# print(ans)
print(*ans[1:])