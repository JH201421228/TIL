import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(arr)
    arr.reverse()
    arr = arr+arr
    print(arr)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()