import sys
input = sys.stdin.readline

vol_A, vol_B = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

print(len((A_set-B_set)|(B_set-A_set)))