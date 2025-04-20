import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


sieve = [1] * 1_299_710
sieve[0] = 0
for n in range(2, int(1_299_710**0.5)+1):
    if sieve[n]:
        for m in range(n**2, 1_299_710, n):
            sieve[m] = 0

cur, pre = 1, 1
arr = [0] * 1_299_710
for idx in range(1, 1_299_710):
    if sieve[idx]:
        arr[pre:cur+1] = [cur-pre+1] * (cur-pre+1)
        cur, pre = idx, idx
    else:
        cur = idx

for _ in range(int(input())):
    n = int(input())
    if sieve[n]: print(0)
    else: print(arr[n])