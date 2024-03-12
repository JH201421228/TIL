import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
liquid_vals = list(map(int, input().split()))
liquid_vals.sort()
# print(liquid_vals)

num = float('inf')

while True:
    val = liquid_vals.pop()
    if not liquid_vals:
        break
    N -= 1
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) >> 1
        if val + liquid_vals[mid] < 0:
            start = mid + 1
        else:
            end = mid - 1
    if abs(val + liquid_vals[end]) < num:
        num = abs(val + liquid_vals[end])
        ans = [val, liquid_vals[end]]
ans.sort()
print(*ans)