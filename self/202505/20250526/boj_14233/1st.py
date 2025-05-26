import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = float("inf")

    for i in range(1, N+1):
        ans = min(ans, arr[i-1]//i)

    print(ans)

    return

if __name__ == "__main__":
    solve()