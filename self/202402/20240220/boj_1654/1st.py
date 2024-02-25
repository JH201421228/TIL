import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, C = map(int, input().split())
home_cordinate = []
check = [0] * N
check[0] = check[-1] = 1

for _ in range(N):
    home_cordinate.append(int(input()))

def find_dist(a, b, c):
