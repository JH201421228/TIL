import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    res = [1] * 10_001

    for idx in range(2, 10_001):
        res[idx] += res[idx-2]

    for idx in range(3, 10_001):
        res[idx] += res[idx-3]

    return res


def init():
    vec = solve()
    for _ in range(int(input())):
        print(vec[int(input())])

    return


if __name__ == "__main__":
    init()