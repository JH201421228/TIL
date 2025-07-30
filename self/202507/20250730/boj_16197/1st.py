import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    MAP = [list(input().rstrip()) for _ in range(N)]

    init = []
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'o':
                init.append(i)
                init.append(j)

    visited = {}
    visited[(init[0], init[1], init[2], init[3])] = True
    q = deque([(init[0], init[1], init[2], init[3], 0)])
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        a, b, c, d, e = q.popleft()

        if e == 10:
            return -1

        for di, dj in delta:
            aa = a + di
            bb = b + dj
            cc = c + di
            dd = d + dj

            if (aa >= N or aa < 0 or bb >= M or bb < 0) and (cc >= N or cc < 0 or dd >= M or dd < 0):
                continue
            if (aa >= N or aa < 0 or bb >= M or bb < 0) or (cc >= N or cc < 0 or dd >= M or dd < 0):
                return e+1

            if MAP[aa][bb] == '#':
                aa = a
                bb = b

            if MAP[cc][dd] == '#':
                cc = c
                dd = d

            if visited.get((aa, bb, cc, dd), False):
                continue

            visited[(aa, bb, cc, dd)] = True
            q.append((aa, bb, cc, dd, e+1))

    return -1


if __name__ == "__main__":
    print(solve())