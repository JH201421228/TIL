import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, D = map(int, input().split())
P = list(map(int, input().split()))

parents = [0] * (N+1)

for idx in P:
    parents[idx] += 1

ans = 0
for n in parents:
    temp = 0

    while n > D:
        temp += n//D
        n = n // D + n % D

    ans += temp

print(ans)