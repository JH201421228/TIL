import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# 노드에 들어있는 다른 노드의 건설이 완료되어야 현재 노드 건설 가능
# 부모 노드에서 부터 시작하면 됨

for _ in range(int(input())):
    N, K = map(int, input().split())
    Ds = list(map(int, input().split()))
    order_dict = {} # 차수를 보여주는 딕셔너리
    order_list = [[] for _ in range(N + 1)]  # 순서 의존도를 정의하는 배열
    start_point = [True] * (N+1)
    for _ in range(K):
        s, e = map(int, input().split())
        start_point[s] = False
        order_dict[s] = order_dict.get(s, 0) + 1
        order_list[s].append(e)

    print(start_point, order_dict, order_list)
