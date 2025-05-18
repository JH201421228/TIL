import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = [0] * (1001)

arr[1] = 1
arr[2] = 0
arr[3] = 1
arr[4] = 1
arr[5] = 1

for idx in range(6, 1001):
    if not arr[idx-1] * arr[idx-3] * arr[idx-4]: arr[idx] = 1

if arr[N]: print("SK")
else: print("CY")