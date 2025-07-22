import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def xor(n):
    if n % 4 == 0: return n
    elif n % 4 == 1: return 1
    elif n % 4 == 2: return n+1
    else: return 0


def solve():
    a, b = map(int, input().split())

    print(xor(a-1) ^ xor(b))

    return


if __name__ == "__main__":
    solve()