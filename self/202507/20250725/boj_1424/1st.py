import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():

    N = int(input())
    L = int(input())
    C = int(input())

    capa = (C+1) // (L+1)

    capa = min(capa, N)

    if not capa % 13: capa -= 1

    ans = N // capa

    if N % capa:
        rest = (N % capa)
        if rest % 13:
            ans += 1
        else:
            if (capa - 1) % 13:
                ans += 1
            else:
                if rest == capa - 1:
                    ans += 2
                else:
                    ans += 1

    print(ans)

    return


if __name__ == "__main__":
    solve()