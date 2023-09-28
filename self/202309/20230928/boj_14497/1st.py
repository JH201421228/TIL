import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    N, M = map(int, input().split())
    # graph = [[] for _ in range(N+1)]
    distance = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        p1, p2, point = map(int, input().split())
        # graph[p1].append((p2, point))
        # graph[p2].append((p1, point))
        distance[p1][p2] = distance[p2][p1] = point
    K = int(input())
    cordinate = list(map(int, input().split()))
    # print(distance)
    for k in range(1, N+1):
        for j in range(1, N+1):
            for i in range(j, N+1):
                if i == j:
                    distance[i][j] = 0
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[j][i] = distance[i][k] + distance[k][j]
    # for inner in distance:
    #     print(inner)
    # print(cordinate)

    ans_list = [float('inf')]
    for idx in range(1, N+1):
        sum_val = 0
        for where in cordinate:
            sum_val += distance[idx][where]
        ans_list.append(sum_val)
    # print(ans_list)
    print(ans_list.index(min(ans_list)))


