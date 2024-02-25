import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = 1

for idx in range(N-1):
    dp1 = dp2 = [0] * (N-idx)
    dp1[0] = dp2[0] = arr[idx]
    dp1_length = dp2_length = 1

    for i in range(idx+1, N):
        if dp1[dp1_length-1] < arr[i]:
            dp1[dp1_length] = arr[i]
            dp1_length += 1
            continue
        start, end = 0, dp1_length
        while start <= end:
            mid = (start + end) >> 1
            if dp1[mid] > arr[i]:
                end = mid - 1
            else:
                start = mid + 1
        dp1[start] = arr[i]

    for i in range(idx+1, N):
        if dp2[dp2_length-1] > arr[i]:
            dp2[dp2_length] = arr[i]
            dp2_length += 1
            continue
        start, end = 0, dp2_length
        while start <= end:
            mid = (start + end) >> 1
            if dp2[mid] < arr[i]:
                end = mid - 1
            else:
                start = mid + 1
        dp2[end] = arr[i]
    print(dp1_length, dp2_length)

    ans = max(ans, dp1_length + dp2_length - 1)
print(ans)