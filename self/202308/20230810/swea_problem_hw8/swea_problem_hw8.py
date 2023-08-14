import sys
from pprint import pprint
sys.stdin = open('input.txt')


def DFS():
    trace = [0] * 100
    stack = [1]
    trace[0] = 1
    ans = [0]
    while stack:
        start = stack.pop()
        for next in range(100):
            if not trace[next] and matrix[start][next]:
                trace[next] = 1
                stack.append(next)
                ans.append(next)
    if 99 in ans:
        return 1
    else:
        return 0

for _ in range(10):
    tc, E = map(int, input().split())
    E_list = list(map(int, input().split()))
    matrix = [[0] * 100 for _ in range(100)]

    for i in range(E):
        matrix[E_list[2*i]][E_list[2*i+1]] = 1

    print(f'#{tc} {DFS()}')
