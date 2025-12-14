import sys
from functools import cmp_to_key
sys.stdin = open("input.txt")
input = sys.stdin.readline


def cmp(x, y):
    return x[0]*y[1] - x[1]*y[0]


def solve():
    N = int(input())
    
    arr = [(*map(int, input().split()), i+1)for i in range(N)]
    
    arr.sort(key=cmp_to_key(cmp))
    
    ans = [a[2] for a in arr]
    
    print(*ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()