import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
liquid_vals = list(map(int, input().split()))
liquid_vals.sort()

start, end = 0, N - 1
sum_val = liquid_vals[start] + liquid_vals[end]
ans = [liquid_vals[start], liquid_vals[end]]
while start <= end:
    mid = (start + end) >> 1
    if liquid_vals[start] + liquid_vals[end] > 0:
        end = mid - 1
    else:
        start = mid + 1
    if abs(liquid_vals[start] + liquid_vals[end]) < abs(sum_val):
        sum_val = liquid_vals[start] + liquid_vals[end]
        ans = [liquid_vals[start], liquid_vals[end]]
ans.sort()
print(*ans)
