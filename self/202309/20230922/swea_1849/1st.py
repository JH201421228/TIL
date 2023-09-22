import sys
import heapq
sys.stdin = open('input.txt')


def scale_is_not_good_for_u(n1, n2):
    pq = [(0, n1)]
    distance = [float('inf') for _ in range(N+1)]
    distance[n1] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        if now == n2:
            break
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist +weight
                heapq.heappush(pq, (dist+weight, next))
    return distance[n2]


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    scale_list = [list(input().split()) for _ in range(M)]
    # print(scale_list)
    # 가중치가 있는 그래프 생성
    # 다익스트라 알고리즘으로 무게 출력
    ans_list = []
    graph = [[] for _ in range(N+1)]
    for idx in range(M):
        if scale_list[idx][0] == '!':
            a, b, w = map(int, scale_list[idx][1:])
            graph[a].append((b, w))
            graph[b].append((a, -w))
        else:
            a, b = map(int, scale_list[idx][1:])
            ans = scale_is_not_good_for_u(a, b)
            if ans == float('inf'):
                ans_list.append('UNKNOWN')
            else:
                ans_list.append(ans)
    print(f'#{test + 1}', *ans_list)