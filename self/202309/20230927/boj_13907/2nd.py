import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 이차원 배열 만들고 한번에 전부 넣기
# 중간에 잘라내기 잘하고
# DFS로 가는 길에 cost 다 더하고, 몇개의 간선을 거치는지 기록
# 방문 횟수



def Why_I_Do_DFS(node):

    if node == D:
        ans_list


    for idx in range()


N, M, K = map(int, input().split())
S, D = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))
taxs = [0]
tax = 0
for _ in range(K):
    tax += int(input())
    taxs.append(tax)

visited = [0] * (N+1)
visited[S] = 1
ans_list = []

