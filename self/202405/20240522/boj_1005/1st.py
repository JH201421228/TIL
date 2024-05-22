import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# 노드에 들어있는 다른 노드의 건설이 완료되어야 현재 노드 건설 가능
# 부모 노드에서 부터 시작하면 됨

for _ in range(int(input())):
    N, K = map(int, input().split())
    Ds = list(map(int, input().split()))
    order_list = [[] for _ in range(N+1)] # 순서 의존도를 정의하는 배열
    start_point = [True] * (N+1) # 시작 지점이 될 수 있는 포인트
    weight = [0] * (N+1)
    for _ in range(K):
        s, e = map(int, input().split())
        order_list[s].append(e)
        start_point[e] = False
    goal = int(input()) # 여기까지 도달하면 게임 끝
    # print(N, K, Ds, order_list, goal, start_point)

    q = deque([])
    for idx in range(1, N+1):
        if start_point[idx]:
            weight[idx] = Ds[idx-1] # 처음 건설 시간 설정
            q.append(idx) # 현재 대기열에 넣기

    while q:
        now = q.popleft()
        for next in order_list[now]: # 현재 노드에서 갈 수 있는 다음 노드
            q.append(next) # 다음 노드 삽입
            if weight[next] < weight[now] + Ds[next-1]:
                weight[next] = weight[now] + Ds[next-1]
    # print(weight)
    print(weight[goal])

