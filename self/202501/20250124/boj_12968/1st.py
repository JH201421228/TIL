import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


R, C, K = map(int, input().split())

if K == 1:
    print(1)
    exit(0)

if (R*C)%2:
    print(0)
    exit(0)

print(1)