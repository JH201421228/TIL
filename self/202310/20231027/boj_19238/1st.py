import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, F = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
# print(MAP)
s_i, s_j = map(int, input().split())
drive = []
for _ in range(M):
    c_s_i, c_s_j, c_e_i, c_e_j = map(int, input().split())
    drive.append((c_s_i, c_s_j, c_e_i, c_e_j))
# print(drive)

