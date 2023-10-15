import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    q = deque([(0, 0)])
    visited = [[0] * N for _ in range(2)]
    visited[0][0] = 1

N, K = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(2)]
# print(board)
print(bfs())