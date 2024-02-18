import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n, k = map(int, input().split())

ans = 1
for i in range(k):
    ans *= n-i
for i in range(k):
    ans //= i+1
print(ans % 10_007)