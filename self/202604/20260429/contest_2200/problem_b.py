import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    
    sorted_arr = sorted(arr)
    
    if arr == sorted_arr: print(N)
    else: print(1)
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()