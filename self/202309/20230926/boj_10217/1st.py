import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def KCM():
    pq = [(0, 0, 1)]
    time_line = [[float('inf') for _ in range(M + 1)] for _ in range(N + 1)]
    time_line[1][0] = 0

    # time_line[i][j] = i노드에 j비용으로 가는 코스트 최저값
    # 근데 j 비용이 50에 100기록됐다치면 j~M까지 전부 100초기하

    while pq:
        time, dist, now = heapq.heappop(pq)
        if time > time_line[now][dist]:
            continue

        if now == N:
            return time

        for next, weight, next_time in graph[now]:
            new_dist = dist + weight
            new_time = time + next_time

            if new_dist <= M and new_time < time_line[next][new_dist]:
                for idx in range(new_dist, M + 1):
                    if time_line[next][idx] > new_time:
                        time_line[next][idx] = new_time
                    else:
                        break
                heapq.heappush(pq, (new_time, new_dist, next))

    return 'Poor KCM'


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(K):
        start, end, point, time = map(int, input().split())
        graph[start].append((end, point, time))

    result = KCM()
    print(result)