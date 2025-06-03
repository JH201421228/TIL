import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def prime_checker(n):
    res = [1] * (n+1)
    res[1] = 0

    for i in range(2, int((n+1)**0.5)+1):
        if res[i]:
            for j in range(i**2, n+1, i): res[j] = 0

    return res


def solve():
    N = int(input())

    is_prime = prime_checker(N)

    ans, pre, cur = {'B': 0, 'S': 0}, 0, 0
    for idx in range(1, N+1):
        if not is_prime[idx]:
            cur = 'B'
            ans['B'] += 1
        else:
            cur = 'S'
            ans['S'] += 1
            if pre == 'B':
                ans['B'] -= 1
                ans['S'] += 1

        pre = cur

    print(ans['B'], ans['S'])

    return


if __name__ == "__main__":
    solve()