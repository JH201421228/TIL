import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))

for idx in range(N):
    if idx % K != arr[idx] % K:
        print("No")
        exit(0)
else:
    print("Yes")