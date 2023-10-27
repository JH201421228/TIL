def dfs(now):
    ret = 1
    for next in v[now]:
        if visited[next]:
            continue
        visited[next] = True
        ret += dfs(next)
    return ret

N = int(input())
if N == 1:
    print("0")
else:
    cnt = 0
    v = [[] for _ in range(50)]
    visited = [False] * 50

    for i in range(N):
        a = input()
        for t in range(len(a)):
            if a[t] == 'Y':
                v[i].append(t)
                cnt += 1

    cnt //= 2
    s = []

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            s.append(dfs(i))

    sum = 0
    for a in s:
        sum += a - 1
        if a == 1:
            print("-1")
            exit()

    if len(s) - 1 <= cnt - sum:
        print(len(s) - 1)
    else:
        print("-1")
