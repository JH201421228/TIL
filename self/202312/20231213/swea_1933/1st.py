import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

ans = []
for i in range(1, n+1):
    if n % i == 0:
        ans.append(i)

print(*ans)