import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    print(max(nums) * min(nums))
    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()