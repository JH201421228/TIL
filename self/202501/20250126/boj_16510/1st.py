import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def binary_search(v):
    s, e = 0, N-1

    while s <= e:
        mid = (s+e) >> 1

        if L[mid] > v:
            e = mid-1
        else:
            s = mid+1

    return e+1


N, M = map(int, input().split())
L = list(map(int, input().split()))

for i in range(1, N):
    L[i] += L[i-1]

for _ in range(M):
    print(binary_search(int(input())))