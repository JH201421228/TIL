import sys
sys.stdin = open('input.txt')


def maze_runner():
    pass

N, M = map(int, input().split())
maze = [list(map(int, map(str, input()))) for _ in range(M)]
print(maze)