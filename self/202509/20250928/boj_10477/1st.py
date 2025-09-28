import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    A, B = map(int, input().split())
    max_v = max(A, B)
    min_v = min(A, B)

    cur = 0
    while True:
        if (1 << cur)-1 >= max_v: break
        cur += 1

    ans = (1 << (cur+1))-1
    tmp = cur
    while True:
        if min_v > (1 << tmp) - 1: break
        ans -= (1 << tmp) - 1 - min_v
        tmp -= 1

    ans -= min(min_v + 1, (1 << cur) - 1 -max_v)

    print(ans)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()