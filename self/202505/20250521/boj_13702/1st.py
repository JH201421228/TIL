import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
lamps = [int(input()) for _ in range(N)]

l, r = 1, (2**31)-1

while l <= r:
    mid = (l+r)>>1

    ans = 0

    for n in lamps: ans += (n//mid)

    if ans >= M: l = mid+1
    else: r = mid-1

print(r)
