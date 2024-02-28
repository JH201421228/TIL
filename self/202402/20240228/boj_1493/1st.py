import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit()


l, w, h = map(int, input().split())
cube_list = []
for _ in range(int(input())):
    cube_list.append(tuple(map(int, input().split())))
print(cube_list)