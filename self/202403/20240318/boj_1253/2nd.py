import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

if N < 3:
    print(0)
    exit(0)
else:
    for idx in range(2, N):
        start, end = 0, idx-1
        while start < end:
            if arr[start] + arr[end] == arr[idx]:
                pass
print(ans)