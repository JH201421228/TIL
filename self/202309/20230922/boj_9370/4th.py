import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


INF = int(1e9)
def awesome_artist():
    pq = [(0, s)]
    distance = [INF] * (n+1)
    check_list = [0] * (n+1)
    distance[s] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if check_list[now]:
            continue
        check_list[now] = 1

        for next, weight in graph[now]:
            if distance[next] >= dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        p1, p2, point = map(int, input().split())
        if (p1 == h and p2 == g) or (p1 == g and p2 == h):
            point -= 0.1
        graph[p1].append((p2, point))
        graph[p2].append((p1, point))
    canditates = []
    for _ in range(t):
        canditates.append(int(input()))
    distance = awesome_artist()
    ans_list = []
    for num in sorted(canditates):
        # print(num)
        if type(distance[num]) == int:
            continue
        ans_list.append(num)
    # print(distance)
    print(*ans_list)