# scc 알고리즘 사용
# 같은 scc 안에 있는지 확인할 배열 필요

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)


def find_scc(now):
    order[0] += 1
    parent = visited[now] = order[0]
    stack.append(now)

    for next in order_list[now]:
        if not visited[next]:
            parent = min(parent, find_scc(next))
        elif not finished[next]:
            parent = min(parent, visited[next])
            # print('parent: ', parent)

    if parent == visited[now]:
        while stack:
            out = stack.pop()
            check[out] = parent
            finished[out] = 1
            if out == now:
                break

    return parent


for _ in range(int(input())):
    N, M = map(int, input().split())
    order = [0]
    order_list = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    finished = [0] * (N+1)
    check = [0] * (N+1)
    stack = []

    for _ in range(M):
        s, e = map(int, input().split())
        order_list[s].append(e)

    for idx in range(1, N+1):
        if not visited[idx]:
            find_scc(idx)

    check_dict = {i: [] for i in set(check[1:])}
    # print(check_dict)

    for start in range(1, N+1):
        for end in order_list[start]:
            if check[end] != check[start]:
                check_dict[check[end]].append(check[start])
    ans = 0
    for k, v in check_dict.items():
        if not v:
            ans += 1
    print(ans)
