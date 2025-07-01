import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    P, M, F, C = map(int, input().split())

    if (M//P)*C >= F: return ((M//P)*C-C)//(F-C) - ((M//P)*C)//F
    else: return 0


def init():
    for t in range(int(input())):
        print(solve())

    return

if __name__ == "__main__":
    init()