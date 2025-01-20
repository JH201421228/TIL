import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
    print(1)
    exit(0)

for i in range(1, N):
    loc = i-1
    newItem = A[i]

    while 0 <= loc and newItem < A[loc]:
        A[loc+1] = A[loc]
        loc -= 1

        if A == B:
            print(1)
            exit(0)

    if loc+1 != i:
        A[loc+1] = newItem

        if A == B:
            print(1)
            exit(0)

print(0)