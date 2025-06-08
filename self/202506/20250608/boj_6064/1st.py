import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a%b

    return a


def lcm(a, b):
    return (a*b)//gcd(a, b)


def solve():
    for _ in range(int(input())):
        M, N, x, y = map(int, input().split())

        limit = lcm(max(M, N), min(M, N))
        year = 0
        isFind = False
        while year <= limit:
            if not (year+x-y)%N:
                year += x
                isFind = True
                break
            year += M

        if isFind: print(year)
        else: print(-1)

    return


if __name__ == "__main__":
    solve()