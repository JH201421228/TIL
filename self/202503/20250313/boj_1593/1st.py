import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


status = [0] * 58
checker = [0] * 58

g, s = map(int, input().split())

W = input().rstrip()
S = input().rstrip()

cnt, res, ans = 0, 0, 0

for w in W:
    checker[ord(w) - 65] += 1

for c in checker:
    if c: cnt += 1

for idx in range(g):
    status[ord(S[idx]) - 65] += 1

for idx in range(58):
    if status[idx] and status[idx] == checker[idx]: res += 1

if res == cnt: ans += 1

for idx in range(g, s):
    pre = status[ord(S[idx])-65]
    status[ord(S[idx])-65] += 1

    if pre and pre == checker[ord(S[idx])-65]: res -= 1
    elif pre + 1 and pre + 1 == checker[ord(S[idx])-65]: res += 1

    pre = status[ord(S[idx-g]) - 65]
    status[ord(S[idx - g]) - 65] -= 1

    if pre and pre == checker[ord(S[idx-g]) - 65]: res -= 1
    elif pre - 1 and pre - 1 == checker[ord(S[idx-g]) - 65]: res += 1

    if res == cnt: ans += 1

print(ans)