import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def cal(n):
    bi = 2
    cnt = 0
    while True:
        if n < bi:
            return cnt
        bi <<= 1
        cnt += 1


N = int(input())
Ns = list(map(int, input().split()))
P = [0] * 40

for n in Ns:
    P[cal(n)] += 1

dead = (N+1)//2

idx = 0
ans = 0

while True:
    if P[idx] >= dead:
        ans += (idx * dead)
        break
    else:
        ans += (idx * P[idx])
        dead -= P[idx]
        idx += 1

print(ans+1)