import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a%b

    return a


def solve():
    a, b, c = map(int, input().split())
    if max(a, b) < c: return False
    return c % gcd(max(a, b), min(a, b)) == 0


def init():
    for _ in range(int(input())):
        if solve():
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    init()