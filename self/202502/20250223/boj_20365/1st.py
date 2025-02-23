import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
S = list(input().rstrip())
init = S[0]
cnt = 1

isPainting = False

for idx in range(N):
    if S[idx] != init and not isPainting:
        isPainting = not isPainting
        cnt += 1
    elif S[idx] == init and isPainting:
        isPainting = not isPainting

print(cnt)