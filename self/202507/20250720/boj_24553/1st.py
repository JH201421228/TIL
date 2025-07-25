import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def init():
    for _ in range(int(input())): solve()
    return


def solve():
    print(0 if int(input()) % 10 else 1)
    return


if __name__ =="__main__":
    init()