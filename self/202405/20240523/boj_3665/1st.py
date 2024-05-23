import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 팀 전체가 안 들어 있으면 IMPOSSIBLE
# 한번에 q에 2개 이상 들어가면 ?


for _ in range(int(input())):
    N = int(input())
    order_graph = [[] for _ in range(N+1)]
    order_list = [0] * (N+1)
    temp = list(map(int, input().split()))

