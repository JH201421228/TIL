import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())
ans = 1
for i in range(2, n+1):
    ans *= i
print(ans)