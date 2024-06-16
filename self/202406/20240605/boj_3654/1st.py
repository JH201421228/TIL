import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    N, M = map(int, input().split())
    pattern = []
    for _ in range(N):
        pattern.append(list(map(str, input().rstrip())))
    b_n = w_n = 0
