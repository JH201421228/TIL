import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(5_000)

N, M = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(str, input().rstrip())))

tower_cnt = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'T':
            MAP[i][j] = tower_cnt = tower_cnt + 1

graph = [set() for _ in range(4*tower_cnt + 1)] # 타워는 4개 방향으로 포격 가능
# 우측, 하단 + // 좌측, 상단 -
# 가로 방향 (타워 번호 - 1) * 2 + 1
# 세로 방향 (타워 번호 - 1) * 2 + 2
visited = [0] * (4*tower_cnt + 1)
finished = [0] * (4*tower_cnt + 1)
grp_num = [0] * (4*tower_cnt + 1)
stack = []
cnt = val = 0

for i in range(N):
    for j in range(M):
        if MAP[i][j] != '.' and MAP[i][j] != '#':
            l = r = u = d = False
            dx = dy = 1
            while i - dx >= 0: # 위로 검색
                if MAP[i-dx][j] == '#': # 벽 만나면 끝
                    break
                elif MAP[i-dx][j] == 'n' or MAP[i-dx][j] == '.':
                    dx += 1
                else:
                    u = MAP[i-dx][j]
                    break
            dx = dy = 1
            while i + dx < N: # 아래로 검색
                if MAP[i+dx][j] == '#': # 벽 만나면 끝
                    break
                elif MAP[i+dx][j] == 'n' or MAP[i+dx][j] == '.':
                    dx += 1
                else:
                    d = MAP[i+dx][j]
                    break
            dx = dy = 1
            while j - dy >= 0: # 왼쪽으로 검색
                if MAP[i][j-dy] == '#': # 벽 만나면 끝
                    break
                elif MAP[i][j-dy] == 'n' or MAP[i][j-dy] == '.':
                    dy += 1
                else:
                    l = MAP[i][j-dy]
                    break
            dx = dy = 1
            while j + dy < M: # 오른쪽으로 검색
                if MAP[i][j+dy] == '#': # 벽 만나면 끝
                    break
                elif MAP[i][j+dy] == 'n' or MAP[i][j+dy] == '.':
                    dy += 1
                else:
                    r = MAP[i][j+dy]
                    break
            # print(i, j, MAP[i][j])
            # print('l: ', l, '/r: ', r, '/u: ', u, '/d: ', d)

            if MAP[i][j] == 'n':
                if (l and r) or (not l and not r):
                    if u:
                        a = (u-1)*2+2
                        graph[-a].add(a)
                    else:
                        a = -((d-1)*2+2)
                        graph[-a].add(a)
                elif (u and d) or (not u and not d):
                    if l:
                        a = (l-1)*2+1
                        graph[-a].add(a)
                    else:
                        a = -((r-1)*2+1)
                        graph[-a].add(a)
                elif (u or d) and (l or r):
                    if u and l:
                        a, b = (u-1)*2+2, (l-1)*2+1
                    elif u and r:
                        a, b = (u-1)*2+2, -((r-1)*2+1)
                    elif d and l:
                        a, b = -((d-1)*2+2), (l-1)*2+1
                    elif d and r:
                        a, b = -((d-1)*2+2), -((r-1)*2+1)
                    graph[-a].add(b)
                    graph[-b].add(a)
            else:
                if u:
                    a = (MAP[i][j]-1)*2+2
                    graph[-a].add(a)
                if d:
                    a = -((MAP[i][j]-1)*2+2)
                    graph[-a].add(a)
                if l:
                    a = (MAP[i][j]-1)*2+1
                    graph[-a].add(a)
                if r:
                    a = -((MAP[i][j]-1)*2+1)
                    graph[-a].add(a)


def find_scc(now):
    global val, cnt
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
            if out == now:
                break

    return parent

# print(graph)
for idx in range(-2*tower_cnt, 2*tower_cnt+1):
    if idx and not visited[idx]:
        find_scc(idx)
ans_list = [0] * (tower_cnt+1)
for idx in range(1, 2*tower_cnt+1):
    if grp_num[idx] > grp_num[-idx]:
        if idx%2:
            # print((idx+1)//2, ': 왼쪽')
            v = False
        else:
            # print((idx+1)//2, ': 위쪽')
            h = False
    else:
        if idx%2:
            # print((idx+1)//2, ': 오른쪽')
            v = True
        else:
            # print((idx+1)//2, ': 아래쪽')
            h = True
    if not idx % 2:
        if not v and not h:
            ans_list[(idx+1)//2] = 4
        elif v and h:
            ans_list[(idx+1)//2] = 2
        elif not v and h:
            ans_list[(idx+1)//2] = 1
        elif v and not h:
            ans_list[(idx+1)//2] = 3

for i in range(N):
    for j in range(M):
        value = MAP[i][j]
        if value != '.' and value != 'n' and value != '#':
            MAP[i][j] = ans_list[value]

for inner in MAP:
    print(''.join(map(str, inner)))