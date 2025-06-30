import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    P, M, F, C = map(int, input().split())

    if M // (P * (1 - (C/F))) == M / (P * (1 - (C/F))):
        return (M // (P * (1 - (C / F)))) - ((M // P) + (C * (M // P)) // F) - 1
    else:
        return (M // (P * (1 - (C / F)))) - ((M // P) + (C * (M // P)) // F)


def init():
    for _ in range(int(input())):
        print(int(solve()))

    return


if __name__ == "__main__":
    init()