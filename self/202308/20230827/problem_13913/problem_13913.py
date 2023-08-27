import sys
from collections import deque
# sys.stdin = open('input.txt')


def hide_and_seek(N):

    que = deque([N])

    while que:
        now = que.popleft()
        next1 = now - 1
        next2 = now + 1
        next3 = now * 2

        if 0 <= next1 and cordinate[next1] == -1:
            visit_log[next1] = now
            return cordinate[now]
        elif next2 <= 100000 and cordinate[next2] == -1:
            visit_log[next2] = now
            return cordinate[now]
        elif next3 <= 100000 and cordinate[next3] == -1:
            visit_log[next3] = now
            return cordinate[now]

        else:
            if 0 <= next1 and not cordinate[next1]:
                que.append(next1)
                cordinate[next1] = cordinate[now] + 1
                visit_log[next1] = now
            if next2 <= 100000 and not cordinate[next2]:
                que.append(next2)
                cordinate[next2] = cordinate[now] + 1
                visit_log[next2] = now
            if next3 <= 100000 and not cordinate[next3]:
                que.append(next3)
                cordinate[next3] = cordinate[now] + 1
                visit_log[next3] = now


N, K = map(int, input().split())
# print(N, K)
cordinate = [0] * 100001
cordinate[N] = 1
cordinate[K] = -1
visit_log = [0] * 100001

if N == K:
    print(0)
    print(N)
else:
    ans = hide_and_seek(N)
    # print(hide_and_seek(N))
    # print(cordinate[:20])
    # print(visit_log[:20])
    trace = []
    where = K
    for _ in range(ans):
       trace.append(where)
       where = visit_log[where]
    trace.append(N)
    trace.reverse()
    print(ans)
    for num in trace:
        print(num, end=' ')
    print()