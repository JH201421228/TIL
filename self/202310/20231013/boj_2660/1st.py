# 한 노드에서 가장 많은 노드를 거치는 개수가 점수
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited = [0] * (N+1)
    visited[start] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = visited[now]+1
                q.append(next)
    return max(visited)


N = int(input())
graph = [[] for _ in range(N+1)]
while True:
    p1, p2 = map(int, input().split())
    if p1 == -1 and p2 == -1:
        break
    graph[p1].append(p2)
    graph[p2].append(p1)
ans = float('inf')
ans_list = []
for idx in range(1, N+1):
    temp_ans = bfs(idx)
    if ans > temp_ans:
        ans = temp_ans
        ans_list = [idx]
    elif ans == temp_ans:
        ans_list.append(idx)
print(ans-1, len(ans_list))
print(*sorted(ans_list))
