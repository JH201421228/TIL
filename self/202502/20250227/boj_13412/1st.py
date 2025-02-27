import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


for _ in range(int(input())):
    N = int(input())

    ans = 0

    for a in range(1, int(N**.5)+1):
        if not N % a and gcd(N // a, a) == 1:
           ans += 1

    print(ans)