import sys
from itertools import permutations
from collections import deque
sys.stdin = open('input.txt')

# k 12 -> 1, 34 -> 3, 56 -> 5

def where_to_go(x, y, K):
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    que = deque([x, y])
    while que:
        now_x, now_y = que.popleft()
        for dx, dy in delta:



def cost(N, K):
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    check_list = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            pass


Test = int(input())
for test in range(Test):
    N, M = map(int, input().split())
    mapping_list = [list(map(int, input().split())) for _ in range(N)]



