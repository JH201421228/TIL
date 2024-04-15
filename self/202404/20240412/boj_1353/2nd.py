import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

e = 2.7182818459045

S, P = map(int, input().split())

if S == P:
    print(1)
    exit()

if math.pow(e, S / e) < P:
    print(-1)
    exit()

prv = -1
for i in range(2, S + 1):
    cur = math.pow(S / i, i)
    if prv > cur:
        print(-1)
        exit()
    if cur >= P:
        print(i)
        exit()
    prv = cur
