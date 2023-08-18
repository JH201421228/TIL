import sys
from collections import deque
sys.stdin = open('input.txt')


def path_finder(start, end):
    que = deque([start]) # 큐를 생성하고 시작지점을 넣습니다.
    trace[start] = 1 # 시작지점의 방문을 기록합니다.

    while que:
        now = que.popleft() # 현재 노드를 팝합니다.
        for next in range(1, V+1): # 다음 탐색할 노드를 찾습니다.
            if not trace[next] and matrix[now][next]: # 다음 탐색할 노드가 방문기록이 없고, 가는 길이 있다면 탐색합니다.
                if next == end: # 다음 노드가 탐색을 종료할 노드라면
                    return trace[now] # 해당 노드까지의 이동 거리를 반환합니다.
                trace[next] = trace[now] + 1 # 다음 노드는 현재 노드보다 1만큼 더 먼 거리에 있습니다.
                que.append(next) # 큐에 탐색 가능한 노드를 넣어줍니다.
    return 0 # 만약 중간에 리턴하지 못했다면, 즉 탐색하고자 하는 위치로 갈 수 없다면 0을 반환합니다.


Test = int(input())
for test in range(Test):
    V, E = map(int, input().split())
    matrix = [[0] * (V+1) for _ in range(V+1)] # 빈 지도를 생성합니다.
    for _ in range(E): # 간선의 개수 만큼 간선 정보를 받겠습니다.
        p1, p2 = map(int, input().split()) # 연결된 두 노드의 정보를 받습니다.
        matrix[p1][p2] = 1 # 연결된 노드를 지도에 표시합니다.
        matrix[p2][p1] = 1 # 방향성이 없기에 해당 행위를 해줍니다.
    start, end = map(int, input().split()) # 탐색 시작 노드 값과 탐색 종료 노드 값을 받습니다.
    trace = [0] * (V+1) # 방문 기록을 저장할 리스트를 만듭니다.
    print(f'#{test + 1} {path_finder(start, end)}') # 결과를 출력합니다.