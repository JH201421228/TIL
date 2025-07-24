import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a%b

    return a


def isAvailable():
    x, y = map(int, input().split())
    distances = list(map(int, input().split()))

    if len(distances) == 2: n = distances[1]
    else:
        n = distances[1]
        for idx in range(2, len(distances)):
            n = gcd(max(n, distances[idx]), min(n, distances[idx]))

    if not abs(x) % n and not abs(y) % n:
        return True
    else:
        return False


def solve():
    for _ in range(int(input())):
        if isAvailable(): print('Ta-da')
        else: print('Gave up')
    return


if __name__ == "__main__":
    solve()