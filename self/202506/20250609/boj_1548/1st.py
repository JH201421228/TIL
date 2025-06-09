import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = N if N < 3 else 0

    for idx in range(N-2):
        temp = 2
        cur = arr[idx] + arr[idx+1]

        for jdx in range(idx+2, N):
            if cur <= arr[jdx]:
                ans = max(ans, temp)
                break
            temp += 1
        else:
            ans = max(ans, temp)

    print(ans)

    return


if __name__ == "__main__":
    solve()