import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def get_gear(idx):
    return idx % 8


def set_gear(n):
    if n < 0: return 7
    else: return n % 8


def solve():
    gears = [list(map(int, input().rstrip())) for _ in range(4)]
    state = [0, 0, 0, 0]

    for _ in range(int(input())):
        n, w = map(int, input().split())
        temp = [0, 0, 0, 0]
        temp[n-1] = w
        l, r = n-2, n

        while l >= 0:
            if gears[l][get_gear(state[l]+2)] != gears[l+1][get_gear(state[l+1]+6)]:
                temp[l] = -temp[l+1]
                l -= 1
            else: break

        while r < 4:
            if gears[r][get_gear(state[r]+6)] != gears[r-1][get_gear(state[r-1]+2)]:
                temp[r] = -temp[r-1]
                r += 1
            else: break

        for idx in range(4):
            state[idx] = set_gear(state[idx] - temp[idx])

    ans = 0
    for idx in range(4):
        if gears[idx][state[idx]]: ans += (1<<idx)

    print(ans)

    return


if __name__ == "__main__":
    solve()