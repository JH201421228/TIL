import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n, k = map(int, input().split())
arr = [0] * (k+1)
arr[0] = 1
for _ in range(n):
    val = int(input())
    for idx in range(1, k+1):
        if idx >= val:
            arr[idx] += arr[idx - val]
print(arr[-1])