import sys
sys.stdin = open('input.txt')


def how_about_this(a, b, c):
    if b == 1:
        return a % c
    elif b % 2:
        return how_about_this(a, b//2, c) ** 2 * a % c
    else:
        return how_about_this(a, b//2, c) ** 2 % c


A, B, C = map(int, input().split())
print(how_about_this(A, B, C))