import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def holiday(n):
    ans = 0
    for i in range(1, int(n**0.5)+1):
        ans += mu[i]*(n//(i**2))
    return ans


mu = [0] * 1_000_001
mu[1] = 1
for i in range(1, 1_000_001):
    for j in range(i*2, 1_000_001, i):
        mu[j] -= mu[i]

K = int(input())


start, end = 0, 100_000_000_000
while start < end-1:
    mid = (start+end)//2
    if mid - holiday(mid) < K:
        start = mid
    else:
        end = mid
print(end)
