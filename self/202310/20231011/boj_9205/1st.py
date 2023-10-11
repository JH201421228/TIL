import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def beer():
    visited = [0] * (n+2)
    visited[0] = 1

    while que:
        now = que.popleft()
        for next in graph[now]:
            if not visited[next]:
                if next == n + 1:
                    return 'happy'
                visited[next] = 1
                que.append(next)
    return 'sad'


for _ in range(int(input())):
    n = int(input()) # 맥주를 파는 편의점 개수
    cordinate = [tuple(map(int, input().split())) for _ in range(n+2)]
    # print(cordinate)
    # 한번에 갈 수 있는 최대 거리 20 * 50 = 1_000
    # 0번에서 마지막 노드까지 갈 수 있는가?
    # 한번에 갈 수 있는 최대 거리를 넘어서면 갈 수 없는 vertax로 판정
    graph = [[] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(i+1, n+2):
            dist = abs(cordinate[i][0] - cordinate[j][0]) + abs(cordinate[i][1] - cordinate[j][1])
            if dist <= 1_000:
                graph[i].append(j)
                graph[j].append(i)
    que = deque([0])
    print(beer())

