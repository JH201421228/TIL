import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve(n, m):
    if not n % m:
        print(str(n//m) + '.' + '(0)')
        return

    ans = []
    if n >= m:
        ans.append(n // m)
    else:
        ans.append(0)

    cnt = 0

    V = [0] * (m+1)
    V[0] = cnt = cnt + 1

    n %= m
    V[n] = cnt = cnt + 1

    while True:
        n *= 10
        ans.append(n//m)
        n %= m

        if V[n]:
            if not n:
                res = f'{ans[0]}' + '.'
                res += ''.join(list(map(str, ans[1:])))
                res += '(0)'
                print(res)
                return
            cnt = V[n]
            break
        V[n] = cnt = cnt + 1

    res = str(ans[0]) + '.'
    res += ''.join(list(map(str, ans[1:cnt-1])))
    res += '('
    res += ''.join(list(map(str, ans[cnt-1:])))
    res += ')'
    print(res)

    return


def init():
    for _ in range(int(input())):
        solve(*tuple(map(int, input().split())))
    return


if __name__ == "__main__":
    init()