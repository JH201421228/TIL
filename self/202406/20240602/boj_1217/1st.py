import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10_000)


while True:
    N, M = map(int, input().split())
    if not N and not M:
        exit(0)

    graph = [[] for _ in range(2*M + 1)]
    visited = [0] * (2*M + 1)
    finished = [0] * (2*M + 1)
    grp_num = [0] * (2*M + 1)
    stack = []
    cnt = 0
    val = 0

    for _ in range(N):
        a, b = map(int, input().split())
        graph[a].append(-b)
        graph[b].append(-a)


    def find_scc(now):
        global cnt, val
        parent = visited[now] = val = val + 1
        stack.append(now)

        for nxt in graph[now]:
            if not visited[nxt]:
                parent = min(parent, find_scc(nxt))
            elif not finished[nxt]:
                parent = min(parent, visited[nxt])

        if parent == visited[now]:
            cnt += 1
            while stack:
                out = stack.pop()
                finished[out] = 1
                grp_num[out] = cnt
                if out == now:
                    break

        return parent


    for idx in range(-M, M+1):
        if idx and not visited[idx]:
            find_scc(idx)

    ans = 1
    for idx in range(1, M+1):
        if grp_num[-idx] == grp_num[idx]:
            ans = 0
            break

    print(ans)