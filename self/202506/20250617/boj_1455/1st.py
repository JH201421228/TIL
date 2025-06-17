import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    print(N, M)
    
    return


if __name__ == "__main__":
    solve()