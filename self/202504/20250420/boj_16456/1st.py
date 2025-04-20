import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

arr = [0] * (N+1)
arr[1:4] = [1, 1, 2]

for idx in range(4, N+1):
    arr[idx] = (arr[idx-1] + arr[idx-3]) % 1_000_000_009

print(arr[N])