import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def binary_search(n):
    s, e = 0, M-1

    while s <= e:
        mid = (s+e) >> 1
        if A[mid] >= n:
            e = mid-1
        else:
            s = mid+1

    return s+1


N, M = map(int, input().split())

A = list(map(int, input().split()))
for idx in range(1, M):
    A[idx] += A[idx-1]

B = [int(input()) for _ in range(N)]

for b in B:
    if b > A[-1]:
        print("Go away!")
        continue

    print(binary_search(b))