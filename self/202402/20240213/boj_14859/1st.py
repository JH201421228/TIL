import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


mu = [0] * 1_000
mu[1] = 1
for i in range(1, 1_000):
    for j in range(i*2, 1_000, i):
        mu[j] -= mu[i]


def mobious(x):
    ans = 0
    for i in range(1, int(n**.5)+1):
        ans += mu[i]*(n//(i**2))
    return ans


n = int(input())
arr = tuple(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            print(mobious(arr[i]*arr[j]*arr[k]))