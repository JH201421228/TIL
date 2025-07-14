import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def get_gcd(a, b):
    while b:
        a, b = b, a%b

    return a


def solve():
    N, K = map(int, input().split())

    if K > N//2: K = N-K

    gcd = get_gcd(N, K)

    print((N//gcd) * (K//gcd - 1))

    return


if __name__ == "__main__":
    solve()