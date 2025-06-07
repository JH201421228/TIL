import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    l, r = max(arr), sum(arr)

    while l <= r:
        mid = (l+r)>>1

        pre, cnt = 0, 1
        for n in arr:
            if pre+n <= mid: pre += n
            else:
                pre = n
                cnt += 1

        if cnt > M: l = mid+1
        else: r = mid-1

    print(l)

    return


if __name__ == "__main__":
    solve()