import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    n, s, e = map(int, input().split())
    arr.append((s, e))
# print(arr)
arr.sort(key=lambda x: (x[0], -x[1]))
# print(arr)

dp = [0] * (N+1)
dp[0] = arr[0][1]
dp_length = 1

for idx in range(1, N):

    if arr[idx-1][0] == arr[idx][0] and arr[idx-1][1] == arr[idx][1]:
        continue

    if -dp[dp_length-1] <= -arr[idx][1]:
        dp[dp_length] = arr[idx][1]
        dp_length += 1
        continue

    start, end = 0, dp_length
    while start <= end:
        mid = (start + end) >> 1
        if -dp[mid] <= -arr[idx][1]:
            start = mid + 1
        else:
            end = mid - 1
    dp[start] = arr[idx][1]
print(dp_length)