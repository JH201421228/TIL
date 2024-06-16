import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(4_000)


def find_scc(now):
    global cnt, val
    parent = visited[now] = val = val + 1
    stack.append(now)

    for nxt in graph[now]:
        if not visited[nxt]:
            parent = min(parent, find_scc(nxt))
        if not finished[nxt]:
            parent = min(parent, visited[nxt])

    if parent == visited[now]:
        cnt += 1
        while stack:
            out = stack.pop()
            finished[out] = 1
            grp_num[out] = cnt
            if now == out:
                break

    return parent


for _ in range(int(input())):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(2*(N+M)+1)]
    visited = [0] * (2*(N+M)+1)
    finished = [0] * (2*(N+M)+1)
    grp_num = [0] * (2*(N+M)+1)
    stack = []
    cnt = 0
    val = 0

    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == x2 and y1 == y2:
            continue

        if x1 < x2:
            s_y = 1
        elif x1 > x2:
            s_y = -1

        if y1 < y2:
            s_x = 1
        elif y1 > y2:
            s_x = -1

        if x1 == x2:
            graph[-s_x*x1].append(s_x*x1)
            continue
        elif y1 == y2:
            graph[-s_y*(N+y1)].append(s_y*(N+y1))
            continue

        graph[-s_x*x1].append(s_x*x2)
        graph[-s_x*x2].append(s_x*x1)
        graph[-s_x*x1].append(s_y*(N+y1))
        graph[-s_y*(N+y1)].append(s_x*x1)
        graph[-s_y*(N+y2)].append(s_x*x2)
        graph[-s_x*x2].append(s_y*(N+y2))
        graph[-s_y*(N+y2)].append(s_y*(N+y1))
        graph[-s_y*(N+y1)].append(s_y*(N+y2))

    for idx in range(-N-M, N+M+1):
        if idx and not visited[idx]:
            find_scc(idx)

    ans = 'Yes'
    for idx in range(1, N+M+1):
        if grp_num[-idx] == grp_num[idx]:
            ans = 'No'
            break

    print(ans)
    # print(graph)
    # print(visited)
    # print(grp_num)