import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    pre, cur = 0, 0
    min_val = 0
    average = sum(arr) / M
    for idx in range(N):
        if pre+arr[idx] <= average: pre += arr[idx]
        else:
            cur = pre+arr[idx]
            if cur-average >= average-pre:
                min_val = max(min_val, pre)
                pre = arr[idx]
            else:
                min_val = max(min_val, cur)
                pre = 0

    print(min_val)
    return


if __name__ == "__main__":
    solve()