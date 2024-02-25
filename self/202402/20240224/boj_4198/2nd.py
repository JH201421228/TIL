import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
if not N:
    print(0)
else:
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr = arr[-1::-1]
    # print(arr)
    ans = 1


    dp1 = [1] * N
    dp2 = [1] * N
    for i in range(1, N):
        for j in range(0, i):
            if arr[i] > arr[j] and dp1[j] + 1 > dp1[i]:
                dp1[i] = dp1[j] + 1
            if arr[i] < arr[j] and dp2[j] + 1 > dp2[i]:
                dp2[i] = dp2[j] + 1

    # print(dp1)
    # print(dp2)
    for idx in range(1, N):
        ans = max(ans, dp1[idx] + dp2[idx] - 1)
    print(ans)