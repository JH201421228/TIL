import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    x, y = map(int, input().split())
    
    if x%2 and y%2: print("NO")
    else: print("YES")
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()