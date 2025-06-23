import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def set_dp():
    res = [0]
    for i in range(1, 100_000):
        res.append(res[-1]+i)

    return res


def solve():
    res = []
    N = int(input())
    arr = list(map(int, input().split()))
    cur = 0
    state = 0
    for idx in range(1, N):
        if arr[idx] == arr[idx-1]:
            state = 0
            if cur:
                res.append(cur)
                cur = 0
        elif arr[idx] > arr[idx-1]:
            if cur:
                if state == -1:
                    cur += 1
                else:
                    res.append(cur)
                    cur = 1
            else:
                cur += 1
            state = 1
        else:
            if cur:
                if state == 1:
                    cur += 1
                else:
                    res.append(cur)
                    cur = 1
            else:
                cur += 1
            state = -1

    if cur: res.append(cur)

    return res


def init():
    dp = set_dp()

    for _ in range(int(input())):
        sol = solve()
        ans = 0
        while sol:
            ans += dp[sol.pop()]

        print(ans)

    return


if __name__ == "__main__":
    init()