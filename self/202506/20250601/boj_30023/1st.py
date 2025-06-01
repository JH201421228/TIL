import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def flipper(n, arr, ans):
    while arr[n-1] != arr[n]:
        ans += 1
        for idx in range(3):
            arr[n+idx] = (arr[n+idx]+1)%3

    return ans


def solve():
    N = int(input())
    arr = list(input().rstrip())
    ans = float("inf")

    for idx in range(N):
        if arr[idx] == 'R': arr[idx] = 0
        elif arr[idx] == 'G': arr[idx] = 1
        else: arr[idx] = 2

    for t in range(3):
        tmp = t
        temp = [*arr]

        for idx in range(1, N-2):
            tmp = flipper(idx, temp, tmp)

        if temp[0] == temp[-1] and temp[-1] == temp[-2]: ans = min(ans, tmp)

        arr[0], arr[1], arr[2] = (arr[0]+1)%3, (arr[1]+1)%3, (arr[2]+1)%3

    if ans == float("inf"): print(-1)
    else: print(ans)

    return


if __name__ == "__main__":
    solve()