import sys
from collections import deque
# sys.stdin = open('input.txt')


def hide_and_seek(N, K):
    que = deque([])
    trace = [0] * 100001
    point = N

    if N >= K:
        return N - K

    if not K and not N:
        return 0
    # if K and N:
    #     if not K % N:
    #         return 0

    if N:
        while True:
            if point > 100000:
                break
            if point == K:
                return 0
            trace[point] = 1
            que.append(point)
            point *= 2
    else:
        que.append(0)
        trace[0] = 1



    while que:
        now = que.popleft()
        next1 = now - 1
        next2 = now + 1
        # print(now)
        if 0 <= next1 and next1 == K:
            return trace[now]#, trace, 1 #
        elif next2 < 100001 and next2 == K:
            return trace[now]#, trace, 2 #
        else:
            if 0 <= next1 < 100001:
                if not trace[next1]:
                    trace[next1] = trace[now] + 1
                    que.append(next1)
                    point = next1
                    if not point:
                        trace[point] = trace[next1]
                    else:
                        while True:
                            if point > 100000:
                                break
                            if point == K:
                                return trace[now]#, trace, 3 #
                            if not trace[point]:
                                trace[point] = trace[next1]
                                que.append(point)
                            point *= 2

            if next2 < 100001:
                if not trace[next2]:
                    trace[next2] = trace[now] + 1
                    que.append(next2)
                    point = next2
                    while True:
                        if point > 100000:
                            break
                        if point == K:
                            return trace[now]#, trace, 4 #
                        if not trace[point]:
                            trace[point] = trace[next2]
                            que.append(point)
                        point *= 2
    return trace


N, K = map(int, input().split()) # N 수빈이 K 동생
print(hide_and_seek(N, K))
# print(trace)

