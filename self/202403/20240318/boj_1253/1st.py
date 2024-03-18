import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

for idx in range(N):
    start, end = 0, N-1
    while start < end:
        sum_val = arr[start] + arr[end]
        if start == idx:
            start += 1
        elif end == idx:
            end -= 1
        else:
            if sum_val == arr[idx]:
                ans += 1
                break
            elif sum_val > arr[idx]:
                end -= 1
            else:
                start += 1
print(ans)