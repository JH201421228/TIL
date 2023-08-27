import sys
from collections import deque
sys.stdin = open('input.txt')

def idiot(N):
    que = deque([1])

    clip_board = 0
    while que:
        now = que.popleft()
        clip_board = now[0]
        next1 = now[0] - 1
        next2 = now[0] + clip_board
        next3 = now[0] + now[1]

        if next1 == N or next2 == N or next3 == N:
            return check[now]
        else:
            if 0 < next1 and (not check[next1] or check[next2] > check[now] + 1):
                check[next1][0] = check[now] + 1
                que.append(next1)
            if next2 < 1001 and not check[next2]:
                check[next2] = check[now] + 2
                que.append(next2)


N = int(input())
check = [[0, 0] for _ in range(1001)]
check[1][0] = 1
# print(N)
print(idiot(N))
print(check[:100])