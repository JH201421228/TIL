import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    arr = list(map(int, input().split()))
    
    print(-sum(arr) + 2 * max(arr))
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()