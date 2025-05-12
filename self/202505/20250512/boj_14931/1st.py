import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


L = int(input())
arr = list(map(int, input().split()))

ans_v, ans_idx = 0, 0

interval = 1

while True:
    if interval > L: break

    temp = 0
    for idx in range(interval-1, L, interval):
        temp += arr[idx]

    if temp > ans_v:
        ans_v = temp
        ans_idx = interval

    interval += 1

if ans_v: print(ans_idx, ans_v)
else: print(0, 0)