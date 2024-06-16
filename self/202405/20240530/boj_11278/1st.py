import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100_000)


def find_scc(now):
    global order, grp_cnt
    parent = visited[now] = order = order + 1
    stack.append(now)

    for nxt in graph[now]:
        if not visited[nxt]:
            parent = min(parent, find_scc(nxt))
        elif not finished[nxt]:
            parent = min(parent, visited[nxt])

    if parent == visited[now]:
        grp_cnt += 1
        while stack:
            out = stack.pop()
            grp_num[out] = grp_cnt
            finished[out] = 1
            if out == now:
                break

    return parent


N, M = map(int, input().split())

graph = [[] for _ in range(2*N+1)]
finished = [0] * (2*N + 1)
visited = [0] * (2*N + 1)
grp_num = [0] * (2*N + 1)
stack = []
order = 0
grp_cnt = 0

for _ in range(M):
    p1, p2 = map(int, input().split())
    graph[-p1].append(p2)
    graph[-p2].append(p1)

for idx in range(-N, N+1):
    if idx and not visited[idx]:
        find_scc(idx)

for idx in range(1, N+1):
    if grp_num[-idx] == grp_num[idx]:
        print(0)
        exit(0)

print(1)
ans = []
for idx in range(1, N+1):
    if grp_num[idx] > grp_num[-idx]:
        ans.append(0)
    else:
        ans.append(1)

print(*ans)