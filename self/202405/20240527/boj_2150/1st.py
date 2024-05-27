import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10_000)


V, E = map(int, input().split())
order = [0]
order_list = [[] for _ in range(V+1)]
visited = [0] * (V+1)
finished = [0] * (V+1)

stack = []
ans = []

for _ in range(E):
    s, e = map(int, input().split())
    order_list[s].append(e)

# print(order_list)
def find_scc(now):
    order[0] += 1
    parent = visited[now] = order[0] # 자기 자신이랑만 연결된 애가 있으므로 parent 있어야함
    stack.append(now)

    for next in order_list[now]:
        if not visited[next]: # 방문한적 없으면 계속 방문
            parent = min(parent, find_scc(next)) # 가장 작은 값을 계속 가지고 다니기 위해서 visited[now] 대신 parent 를 사용
        elif not finished[next]: #
            parent = min(parent, visited[next])

    if parent == visited[now]: # 가장 먼저 들어온 값을 체크(스택에는 순서대로 넣었기 때문)
        temp = []

        while stack:
            out = stack.pop()
            finished[out] = 1 # 참으로 변경
            temp.append(out)
            if now == out:
                break
        temp.sort()
        temp.append(-1)
        ans.append(temp)
    return parent

for idx in range(1, V+1):
    if not visited[idx]:
        find_scc(idx)
ans.sort()
print(len(ans))
for inner in ans:
    print(*inner)

