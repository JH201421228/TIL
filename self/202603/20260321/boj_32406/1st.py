import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    cur_a = a[-1] + b[-2]
    cur_b = b[-1] + a[-2]
    
    ans = abs(cur_a - cur_b)
    
    for idx in range(N-2):
        ans += abs(a[idx]-b[idx])
    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()