import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    print(input().rstrip() * N)
    
    return


def main():
    
    solve()
    
    return


if __name__ == "__main__":
    main()