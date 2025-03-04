import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
J = list(int(input()) for _ in range(M))

l, r = 1, max(J)

while l <= r:
    mid = (l+r) >> 1

    total = sum(j//mid + 1 if j%mid else j//mid for j in J)

    if total <= N:
        r = mid-1
    else:
        l = mid+1

print(l)