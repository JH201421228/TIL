import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


def quadrant(x, y):
    if not x:
        if y > 0: return 0, 1
        else: return 0, -1
    elif not y:
        if x > 0: return 1, 0
        else: return -1, 0

    n = gcd(max(abs(x), abs(y)), min(abs(x), abs(y)))
    return x//n, y//n


def solve():
    N = int(input())

    ans_dict = {}

    for _ in range(N):
        a, b = map(int, input().split())
        k = quadrant(a, b)
        ans_dict[k] = ans_dict.get(k, 0) + 1

    ans = 0

    for k ,v in ans_dict.items():
        ans = max(ans, v)

    print(ans)

    return


if __name__ == "__main__":
    solve()