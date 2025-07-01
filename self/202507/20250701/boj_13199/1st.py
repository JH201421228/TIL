import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    P, M, F, C = map(int, input().split())
    s = (M // P) * C
    s = (s // F) * C + s % F
    res = 0

    while s >= F:
        res += s // F
        s = (s // F) * C + s % F

    return res

def init():
    for t in range(int(input())):
        print(solve())

    return

if __name__ == "__main__":
    init()