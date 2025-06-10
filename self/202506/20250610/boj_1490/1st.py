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
    N = int(input())

    n = N
    lcm_n = 1
    while n:
        m = n % 10
        n //= 10

        if m: lcm_n = lcm(max(lcm_n, m), min(lcm_n, m))

    ans = N
    cnt = 0
    while True:
        if not ans % lcm_n:
            print(ans)
            break

        ans *= 10
        cnt += 1
        if ans % lcm_n:
            m = lcm_n - (ans % lcm_n)
            if len(str(m)) <= cnt: ans += m

    return


if __name__ == "__main__":
    solve()