import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


P, N = map(int, input().split())
S = list(map(int, input().split()))
S.sort()

l = len(S)
cur = P-1
idx = 0
ans = 0
while cur > 0:
    if cur - S[idx] >= 0:
        ans += cur
        cur -= S[idx]
        idx += 1
        if idx == l:
            break
    else:
        break


print(idx, ans)