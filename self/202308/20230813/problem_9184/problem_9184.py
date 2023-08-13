import sys
sys.stdin = open('input.txt')

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        return w(a, b, c - 1) + w(a, b - 1, c) + w(a, b - 1, c - 1)
