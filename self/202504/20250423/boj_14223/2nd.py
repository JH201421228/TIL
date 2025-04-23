import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

ans = float("inf")

for i in range(N-1):
    for j in range(i+1, N):
        max_x, min_x, max_y, min_y = -float("inf"), float("inf"), -float("inf"), float("inf")
        for idx in range(N):
            if idx == i or idx == j: continue
            max_x, min_x, max_y, min_y = max(max_x, arr[idx][0]), min(min_x, arr[idx][0]), max(max_y, arr[idx][1]), min(min_y, arr[idx][1])

        ans = min(ans, max(max_x-min_x, max_y-min_y))

print((ans+2)**2)