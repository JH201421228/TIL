import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

dp = [0] * (N+1)
dp[0] = arr[0]
dp_length = 1
check = [1] * N

for idx in range(1, N):
    if dp[dp_length - 1] < arr[idx]:
        dp[dp_length] = arr[idx]
        dp_length += 1
        check[idx] = dp_length
        continue
    start, end = 0, dp_length
    while start <= end:
        mid = (start + end) >> 1
        if dp[mid] < arr[idx]:
            start = mid + 1
        else:
            end = mid - 1
    dp[start] = arr[idx]
    check[idx] = start + 1
print(arr)
print(dp)
print(check)
print(dp_length)