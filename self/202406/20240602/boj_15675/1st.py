import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(5_000)


N, M = map(int, input().split())
graph = [[] for _ in range(2*(N+M) + 1)]
finished = [0] * (2*(N+M) + 1)
visited = [0] * (2*(N+M) + 1)
cnt = 0
val = 0
grp_num = [0] * (2*(N+M) + 1)
stack = []


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


for i in range(1, N+1):
    temp = list(map(str, input().rstrip()))
    for j in range(1, M+1):
        if temp[j-1] == '*':
            graph[-i].append(N+j)
            graph[-N-j].append(i)
            graph[i].append(-N-j)
            graph[N+j].append(-i)
        elif temp[j-1] == '#':
            graph[i].append(N+j)
            graph[-N-j].append(-i)
            graph[-i].append(-N-j)
            graph[N+j].append(i)

for idx in range(-N-M, N+M+1):
    if idx and not visited[idx]:
        find_scc(idx)

for idx in range(1, N+M+1):
    if grp_num[-idx] == grp_num[idx]:
        print(0)
        exit(0)

print(1)