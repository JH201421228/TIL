import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

arr = [0] * 11
for _ in range(2047):
    temp = list(map(int, input().split()))
    for idx in range(11):
        arr[idx] ^= temp[idx]

print(*arr)