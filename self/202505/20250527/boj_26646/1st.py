import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for idx in range(1, N):
        h1, h2 = arr[idx-1], arr[idx]
        ans += (h1+h2)**2 + abs(h1-h2)**2

    return ans


if __name__ == "__main__":
    print(solve())