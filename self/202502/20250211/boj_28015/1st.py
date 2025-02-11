import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def drawing(L):
    q = deque(L)
    res = 0

    while q:
        cur = q[0]
        while q and q[0] == cur:
            q.popleft()

        while q and q[-1] == cur:
            q.pop()

        res += 1

    return res


N, M = map(int, input().split())

draws = [list(map(int, input().rstrip().split())) for _ in range(N)]

ans = 0

for draw in draws:
    temp = []
    for pix in draw:
        if pix == 0:
            if temp:
                ans += drawing(temp)
                temp = []
        else:
            temp.append(pix)
    if temp:
        ans += drawing(temp)

print(ans)
# ejel = [''.join(i) for i in ejel]
# ejel = [i.split('0') for i in ejel]
#
# for eje in ejel:
#     for ej in eje: