import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T, W = map(int, input().split())
L = []

for i in range(T):
    L.append(int(input()))

print(L)

