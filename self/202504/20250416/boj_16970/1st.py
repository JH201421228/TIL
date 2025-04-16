import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a%b

    return a


N, M, K = map(int, input().split())

ans = 0
temp = 0

for i in range(N+1):
    for j in range(M+1):
        for ii in range(i, N+1):
            for jj in range(j, M+1):
                x, y = ii-i, jj-j
                if x or y:
                    if (not x or not y) and (x+1 == K or y+1 == K):
                        ans += 1
                    elif gcd(max(x, y), min(x, y))+1 == K:
                        temp += 1

print(ans + 2*temp)