import sys
from collections import deque
sys.stdin = open('input.txt')


def did_we_friend(start):
    que = deque([start])

    while que:
        now = que.popleft()
        for next in graph[now]:
            if not check_list[next]:
                check_list[next] = 1
                que.append(next)


T = int(input())
for test in range(T):
    N, relationship = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(relationship):
        r1, r2 = map(int, input().split())
        graph[r1].append(r2)
        graph[r2].append(r1)
    # print(graph)
    check_list = [0] * (N + 1)
    ans = 0
    for man in range(1, N + 1):
        if not check_list[man]:
            did_we_friend(man)
            ans += 1
    print(f'#{test + 1} {ans}')
