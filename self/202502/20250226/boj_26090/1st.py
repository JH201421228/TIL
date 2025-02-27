import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def isPrime():
    top = int((500*2000)**.5)+1
    for i in range(2, top):
        if primeArr[i]:
            idx = 2*i
            while idx < 500 * 2000 + 1:
                primeArr[idx] = 0
                idx += i


N = int(input())
arr = list(map(int, input().split()))
arrPrime = [0]
primeArr = [1] * (500 * 2000 + 1)
primeArr[0] = 0
primeArr[1] = 0

for idx in range(N):
    arrPrime.append(arrPrime[-1] + arr[idx])

isPrime()

ans = 0

for idx in range(2, N+1):
    if primeArr[idx]:
        l = idx
        while l < N+1:
            if primeArr[arrPrime[l] - arrPrime[l-idx]]:
                ans += 1
            l += 1

print(ans)