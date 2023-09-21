import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


n, m, r = map(int, input().split())
how_many_item = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
