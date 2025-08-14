import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def paper_count(arr, L):
    cnt = 0

    cur = 0
    while cur < len(arr):
        if arr[cur]:
            cnt += 1
            cur += L
            continue
        cur += 1

    return cnt


def solve():
    N, M = map(int, input().split())
    K = int(input())

    arr = [0] * M
    height = 0

    for _ in range(int(input())):
        x, y = map(int, input().split())

        height = max(height, x)
        arr[y-1] = 1

    s, e = height, max(N, M)

    while s <= e:
        mid = (s+e) >> 1

        if paper_count(arr, mid) > K:
            s = mid+1
        else:
            e = mid-1

    print(s)

    return


if __name__ == "__main__":
    solve()