import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    cards = list(map(int, input().split()))

    arr = [0] * (N+1)
    arr[1] = cards[0]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if i-j >= 0: arr[i] = max(arr[i], arr[i-j] + cards[j-1])

    print(arr[-1])

    return


if __name__ == '__main__':
    solve()