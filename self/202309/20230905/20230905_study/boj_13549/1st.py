import sys
from collections import deque
# sys.stdin = open('input.txt')


def hide_and_seek(N, K):
    que = deque([])
    trace = [0] * 100001 # 방문 지점을 다시 방문하지 않기 위한 리스트 생성
    point = N

    # edge case
    if N >= K: # 수빈이가 동생보다 앞에 있다면 -1 로만 동생을 찾을 수 있음
        return N - K

    if not K and not N: # 수빈이와 동생 둘다 0좌표에 있다면
        return 0
    # if K and N:
    #     if not K % N:
    #         return 0


    # edge case


    if N: # 수빈이의 최초 좌표가 0이 아니라면
        while True: # 최초 좌표의 2배로 갈 수 있는 모든 지역에 체크 및 탐사 지점 추가
            if point > 100000:
                break
            if point == K:
                return 0
            trace[point] = 1
            que.append(point) # 탐사지점 추가
            point *= 2
    else: # 수빈이의 최초 좌표가 0이면
        que.append(0) # 0을 탐사 지점 추가
        trace[0] = 1



    while que: # que에 값이 있는 동안
        now = que.poplft() # 현재 값
        next1 = now - 1 # 다음 조사할 값 (1초 사용)
        next2 = now + 1 # 다음 조사할 값 (1초 사용)
        # print(now)
        if 0 <= next1 and next1 == K: # 다음 조사 대상에 동생이 있다면
            return trace[now]#, trace, 1 # 걸린 시간을 반환
        elif next2 < 100001 and next2 == K:
            return trace[now]#, trace, 2 #
        else:
            if 0 <= next1 < 100001: # 인덱스 유효성 검사
                if not trace[next1]: # 아직 간적 없는 곳이라면,
                    trace[next1] = trace[now] + 1 # 걸린 시간 + 1
                    que.append(next1) # 다음 조사할 위치에 추가
                    point = next1 # 순간이동을 위한 준비
                    if not point: # point가 0이면
                        trace[point] = trace[next1] # 그냥 넘어감
                    else:
                        while True:
                            if point > 100000: # point 가 유효한 범위에 있는 동안
                                break
                            if point == K: # 순간이동하면서 동생을 찾는다면,
                                return trace[now]#, trace, 3 # 걸린 시간을 반환
                            if not trace[point]: # 순간이동 장소가 처음 오는 곳이라면,
                                trace[point] = trace[next1] # 시간을 기록
                                que.append(point) #다음 탐사 가능지점 추가
                            point *= 2 # 2배 위치로 순간이동

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