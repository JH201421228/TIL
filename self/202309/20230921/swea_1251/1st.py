import sys
import heapq
sys.stdin = open('input.txt')


def anne_marie_Perfect_to_Me():
    pq = [(0, 0)]
    check_list = [0] * N
    ans = 0
    cnt = 0

    while pq:
        if cnt == N:
            break
        dist, now = heapq.heappop(pq)
        if check_list[now]:
            continue
        check_list[now] = 1
        ans += dist
        cnt += 1
        for weight, next in graph[now]:
            if not check_list[next]:
                heapq.heappush(pq, (weight, next))
    return ans


T = int(input())
for test in range(T):
    N = int(input())
    cordinate_info = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            dis = E * ((cordinate_info[0][i] - cordinate_info[0][j])**2 + (cordinate_info[1][i] - cordinate_info[1][j])**2)
            graph[i].append((dis, j))
            graph[j].append((dis, i))
    # print(graph)
    print(f'#{test+1} {round(anne_marie_Perfect_to_Me())}')