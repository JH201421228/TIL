import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100_000)

N, M = map(int, input().split())
state = [0]
state += list(map(int, input().split()))
room = [[] for _ in range(N+1)]
for idx in range(1, M+1):
    temp = list(map(int, input().split()))
    for r in temp[1:]:
        room[r].append(idx)
# print(room)
# print(state)

graph = [[] for _ in range(2*M + 1)]
for idx in range(1, N+1):
    if not state[idx]:
        graph[-room[idx][0]].append(room[idx][1])
        graph[-room[idx][1]].append(room[idx][0])
        graph[room[idx][0]].append(-room[idx][1])
        graph[room[idx][1]].append(-room[idx][0])
    else:
        graph[room[idx][0]].append(room[idx][1])
        graph[room[idx][1]].append(room[idx][0])
        graph[-room[idx][0]].append(-room[idx][1])
        graph[-room[idx][1]].append(-room[idx][0])

visited = [0] * (2*M + 1)
finished = [0] * (2*M + 1)
cnt = 0
val = 0
grp_num = [0] * (2*M + 1)
stack = []

def find_scc(now):

    global cnt, val
    stack.append(now)
    parent = visited[now] = cnt = cnt + 1

    for nxt in graph[now]:
        if not visited[nxt]:
            parent = min(parent, find_scc(nxt))
        elif not finished[nxt]:
            parent = min(parent, visited[nxt])

    if parent == visited[now]:
        val += 1
        while stack:
            out = stack.pop()
            finished[out] = 1
            grp_num[out] = val
            if out == now:
                break

    return parent

for idx in range(-M, M+1):
    if idx and not visited[idx]:
        find_scc(idx)

# print(graph)
# print(grp_num)
# print(visited)
# print(finished)
for idx in range(1, M+1):
    if grp_num[-idx] == grp_num[idx]:
        print(0)
        exit(0)

print(1)