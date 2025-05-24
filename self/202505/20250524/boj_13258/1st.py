import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    J = int(input())
    C = int(input())

    return arr[0] + (J * C * arr[0]) / sum(arr)


if __name__ == "__main__":
    print(solve())