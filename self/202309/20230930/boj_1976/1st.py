import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def holiday(start):
    que = deque([start])
    visited = [0] * N
    visited[start] = 1

    while que:
        now = que.popleft()
        for next in range(N):
            if graph[now][next] and not visited[next]:
                visited[next] = 1
                que.append(next)
    return visited


N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visit = list(map(int, input().split()))
visited = holiday(visit[0]-1)
flag = 0
for idx in range(1, M):
    if not visited[visit[idx]-1]:
        flag = 1
        break
if flag:
    print('NO')
else:
    print('YES')
# 시작 도시부터 방문을 시작하면서 방문 가능한 도시를 체크
# 방문 가능 도시를 체크한 리스트를 반환하는 함수
# 여행할 도시들이 방문 리스트에 있는지 확인