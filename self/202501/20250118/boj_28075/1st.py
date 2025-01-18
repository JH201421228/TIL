import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(o, v, pre):
    global N, M, cnt

    if o > N:
        if v >= M:
            cnt += 1
        return

    if v >= M:
        cnt += 6**(N-o+1)
        return

    for i in range(6):
        x, y = i // 3, i % 3

        if pre == y:
            dfs(o+1, v+(G[x][y]>>1), y)
        else:
            dfs(o+1, v+G[x][y], y)

    return

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(2)]

cnt = 0
dfs(1, 0, -1)

print(cnt)