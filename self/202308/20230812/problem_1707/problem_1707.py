import sys
# from pprint import pprint as print
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        vertex1, vertex2 = map(int, input().split())
        graph[vertex1][vertex2] = 1
        graph[vertex2][vertex1] = 1

    print(graph)