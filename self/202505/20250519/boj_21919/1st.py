import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


MAX_N = 1_000_000
sieve = [1] * (MAX_N+1)
sieve[0], sieve[1] = 0, 0

for n in range(2, int(MAX_N**0.5)+1):
    if sieve[n]:
        for m in range(n**2, MAX_N+1, n):
            sieve[m] = 0

N = int(input())
arr = list(map(int, input().split()))

ans = 1

for n in arr:
    if sieve[n]: ans *= n

if ans == 1: print(-1)
else: print(ans)