import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def maze_runner(x, y):
    s = [(x, y)]

    while s:
        x, y = s.pop()



N, M = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * (M+2) for _ in range(N+2)]

for i in range(1, M+1):
    while True:
        if not visited[0][i]:
            visited[0][i] = 1
