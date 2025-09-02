import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dq(n, cur):
    if n == 1:
        res = [(0, 0), (0, 1), (1, 1), (1, 0)]
        return res[cur-1]

    L = 2**(n-1)
    area = L**2
    x, y = dq(n-1, (cur-1) % area + 1)
    if cur <= area: return (y, x)
    elif cur <= 2*area: return (x, y+L)
    elif cur <= 3*area: return (x+L, y+L)
    return (2*L-y-1, L-x-1)


def cal_dist(a, b, c, d):
    return round((((a-c) ** 2 + (b-d) ** 2) ** .5) * 10)


def solve():
    n, h, o = map(int, input().split())

    print(cal_dist(*dq(n, h), *dq(n, o)) )

    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()