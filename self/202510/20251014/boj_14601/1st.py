import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


cnt = 1


def set_num(i, j, ti, tj, l, ans):
    global cnt

    res = [[] for _ in range(4)]

    if ti >= i and ti < i+l and tj >= j and tj < j+l:
        pass
    else:
        ans[i+l-1][j+l-1] = cnt
        res[0] = [i+l-1, j+l-1]

    if ti >= i+l and ti < i+l*2 and tj >= j and tj < j+l:
        pass
    else:
        ans[i+l][j+l-1] = cnt
        res[1] = [i+l, j+l-1]

    if ti >= i and ti < i+l and tj >= j+l and tj < j+l*2:
        pass
    else:
        ans[i+l-1][j+l] = cnt
        res[2] = [i+l-1, j+l]

    if ti >= i+l and ti < i+l*2 and tj >= j+l and tj < j+l*2:
        pass
    else:
        ans[i+l][j+l] = cnt
        res[3] = [i+l, j+l]

    cnt += 1

    return res


def dq(i, j, ti, tj, l, ans):
    global cnt

    if l == 1:
        for di in range(2):
            for dj in range(2):
                if not ans[i+di][j+dj]:
                    ans[i+di][j+dj] = cnt
        cnt += 1
        return

    temp = set_num(i, j, ti, tj, l, ans)

    for idx, d in enumerate([[0, 0], [l, 0], [0, l], [l, l]]):
        di, dj = d
        if temp[idx]:
            dq(i+di, j+dj, *temp[idx], l//2, ans)
        else:
            dq(i+di, j+dj, ti, tj, l//2, ans)

    return


def solve():
    K = int(input())
    ti, tj = map(int, input().split())
    ti, tj = 2**K-tj, ti-1

    ans = [[0] * (2**K) for _ in range(2**K)]
    ans[ti][tj] = -1

    dq(0, 0, ti, tj, 2**(K-1), ans)

    for a in ans:
        print(*a)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()