import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(K):
        start, end, point, time = map(int, input().split())
        graph[start].append((end, point, time))

    ans_list = [[float('inf')] * (M+1) for _ in range(N+1)]
    ans_list[1][0] = 0

    for point in range(M+1):
        for now in range(1, N+1):
            if ans_list[now][point] != float('inf'):
                for next, weight, time in graph[now]:
                    if point + weight < M+1 and ans_list[now][point] + time < ans_list[next][point + weight]:
                        ans_list[next][point + weight] = ans_list[now][point] + time
    # for inner in ans_list:
    #     print(inner)
    ans = min(ans_list[-1])
    if ans == float('inf'):
        print('Poor KCM')
    else:
        print(ans)