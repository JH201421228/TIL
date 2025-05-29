import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def recurse(val, length, arr):
    global ans

    if length == 2:
        ans = max(ans, val)
        return

    for idx in range(1, length-1):
        recurse(val+arr[idx-1]*arr[idx+1], length-1, arr[:idx]+arr[idx+1:])

    return


def solve():
    global ans

    N = int(input())
    arr = list(map(int, input().split()))

    recurse(0, N, arr)

    print(ans)

    return


if __name__ == "__main__":
    ans = 0
    solve()