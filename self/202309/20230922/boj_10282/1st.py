import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def computer_virus():
    pq = [(0, c)]
    distance = [float('inf') for _ in range(n+1)]
    distance[c] = 0
    check_list = [0] * (n+1)
    cnt = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if check_list[now]:
            continue
        check_list[now] = 1
        cnt += 1
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return cnt, distance


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        # graph[a].append((b, s))
        graph[b].append((a, s))
    cnt, ans_list = computer_virus()
    ans = 0
    for num in ans_list:
        if num == float('inf'):
            continue
        else:
            if num > ans:
                ans = num
    print(cnt, ans)
