import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
liquid_val = list(map(int, input().split()))
liquid_val.sort()

start, end = 0, N-1
sum_val = liquid_val[start] + liquid_val[end]
ans = [liquid_val[start], liquid_val[end]]
while start < end:
    temp = liquid_val[start] + liquid_val[end]
    if temp == 0:
        break
    elif temp > 0:
        end -= 1
        if end == -1:
            break
    else:
        start += 1
        if start == N:
            break
    if not start == end and abs(liquid_val[start] + liquid_val[end]) < abs(sum_val):
        sum_val = liquid_val[start] + liquid_val[end]
        ans = [liquid_val[start], liquid_val[end]]
ans.sort()
print(*ans)