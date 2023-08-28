import sys
from collections import deque
# sys.stdin = open('input.txt')


def idiot(N):
    que = deque([1])

    while que:
        now = que.popleft()
        next1 = now - 1 # 한개를 지우는 경우
        next2 = now + idiot_list[now][1] # 기존 클립 보드에 저장된 이모티콘을 더하는 경우
        next3 = now * 2 # 현재 모든 클립보드를 복사해서 붙여넣기 하는 경우, 시간은 2가 들고, 클립보드에 저장된 값을 바꿔줘야함

        if next1 == N or next2 == N:
            return idiot_list[now][0]
        elif next3 == N:
            return idiot_list[now][0] + 1
        else:
            if 0 <= next1 and (not idiot_list[next1][0] or idiot_list[next1][0] > idiot_list[now][0] + 1):
                que.append(next1)
                idiot_list[next1] = [idiot_list[now][0] + 1, idiot_list[now][1]]
            if next2 < 3001 and (not idiot_list[next2][0] or idiot_list[next2][0] > idiot_list[now][0] + 1):
                que.append(next2)
                idiot_list[next2] = [idiot_list[now][0] + 1, idiot_list[now][1]]
            if next3 < 3001 and not idiot_list[next3][0]:
                que.append(next3)
                idiot_list[next3] = [idiot_list[now][0] + 2, now]
            if


N = int(input())
idiot_list = [[0, 0] for _ in range(3001)] # [time, clip_board]
idiot_list[1][0] = 1
print(idiot(N))