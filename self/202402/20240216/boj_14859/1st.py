import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


mu = [0] * 1_000_001
mu[1] = 1
for i in range(1, 1_000_001):
    for j in range(i*2, 1_000_001, i):
        mu[j] -= mu[i]


n = int(input())
arr = tuple(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not mu[arr[i]]*mu[arr[j]]*mu[arr[k]]:
                res += 1
print(res)