import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def odinson():
    pq = [()]

    visited = [[0] * (N+1) for _ in range(N+1)]



N, M = map(int, input().split())
cost = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
# print(graph)