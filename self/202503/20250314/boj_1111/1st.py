import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

if N == 1:
    print('A')
    exit(0)

arr = list(map(int, input().split()))

if N == 2:
    if arr[1] == arr[0]:
        print(arr[1])
        exit(0)
    else:
        print('A')
        exit(0)


a = (arr[2] - arr[1]) / (arr[1] - arr[0]) if arr[1] - arr[0] else 0
b = arr[1] - a * arr[0]

idx = 1
cur = arr[idx-1]
while idx < N:
    nxt = a * cur + b

    if arr[idx] == nxt:
        cur = nxt
        idx += 1

    else:
        print('B')
        exit(0)

if int(a) == a and int(b) == b:
    print(int(a * cur + b))
else:
    print('B')