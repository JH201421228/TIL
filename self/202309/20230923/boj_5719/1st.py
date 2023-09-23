import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def anne_marie(S, D):
    pq = [(0, S, '')]
    distance = [float('inf') for _ in range(N)]
    distance[S] = 0

    while pq:
        dist, now, trace = heapq.heappop(pq)

        if distance[now] < dist:
            continue
        if now == D:
            return dist, trace
        for next, weight in graph[now]:
            if next not in prohibit_matrix[now]:
                if distance[next] > weight + dist:
                    distance[next] = weight + dist
                    heapq.heappush(pq, (weight + dist, next, trace + ' ' +str(next)))
    return False, False


while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    S, D = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        start, end, point = map(int, input().split())
        graph[start].append((end, point))

    prohibit_matrix = [[] for _ in range(N)]
    least, route = anne_marie(S, D)
    if least is False:
        print(-1)
        continue
    prohibit = [S]
    prohibit.extend(list(map(int, route.split())))
    for idx in range(len(prohibit) - 1):
        prohibit_matrix[prohibit[idx]].append(prohibit[idx + 1])

    # print(least, route)
    # print(prohibit)
    # print('------------')

    while True:
        l, r = anne_marie(S, D)
        # print(l, r)
        # print('---------------')
        if l is False:
            print(-1)
            break
        elif least == l:
            p = [S]
            p.extend(list(map(int, r.split())))
            for idx in range(len(p) - 1):
                prohibit_matrix[p[idx]].append(p[idx + 1])
            # print(graph)
            # print(prohibit_matrix)
        else:
            print(l)
            break
