import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100_000)
from collections import deque


def find_scc(now):
    global check, order, ans
    parent = visited[now] = order = order + 1
    stack.append(now)

    for nxt in graph[now]:
        if not visited[nxt]:
            parent = min(parent, find_scc(nxt))
        elif not finished[nxt]:
            parent = min(parent, visited[nxt])

    if parent == visited[now]:
        check += 1
        while stack:
            out = stack.pop()
            finished[out] = 1
            grp_num[out] = check
            if now == out:
                break

    return parent


input_list = deque([])
while True:
    try:
        a, b = map(int, input().split())
        input_list.append((a, b))
    except:
        break

while input_list:
    N, M = input_list.popleft()
    graph = [[] for _ in range(2*N+1)]
    finished = [0] * (2*N+1)
    visited = [0] * (2*N+1)
    order = 0
    check = 0
    stack = []
    grp_num = [0] * (2*N+1)
    ans = True

    for _ in range(M):
        a, b = input_list.popleft()
        graph[-a].append(b)
        graph[-b].append(a)

    for idx in range(-N, N+1):
        if idx and not visited[idx]:
            find_scc(idx)

    for idx in range(1, N+1):
        if grp_num[idx] == grp_num[-idx]:
            ans = False
            break

    if not ans:
        print('no')
        continue

    if grp_num[1] > grp_num[-1]:
        ans = False

    if ans:
        print('yes')
    else:
        print('no')
