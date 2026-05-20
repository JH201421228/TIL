import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    arr = list(map(int, input().split()))
    
    ans = [[] for _ in range(4)]
    
    for a in arr:
        if not a % 6: ans[-1].append(a)
        elif not a % 3: ans[2].append(a)
        elif not a % 2: ans[0].append(a)
        else: ans[1].append(a)
        
    print(*ans[0], *ans[1], *ans[2], *ans[3])
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()