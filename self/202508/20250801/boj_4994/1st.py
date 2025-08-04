import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve(N):
    M = 1

    while M < N:
        M *= 10
        M += 1

    while True:
        pass

    return


def init():
    while True:
        N = int(input())

        if N: solve(N)
        else: break


if __name__ == "__main__":
    init()