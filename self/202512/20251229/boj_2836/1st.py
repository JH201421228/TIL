import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    
    ans = M
    arr = []
    
    for _ in range(N):
        a, b = map(int, input().split())
        
        if a > b: arr.append((b, a))
    
    
    arr.sort()
    
    s, e = 0, 0

    for a, b in arr:
        if a <= e:
            e = max(e, b)
        
        else:
            ans += 2 * (e - s)
            s, e = a, b
    
    if e > s: ans += 2 * (e - s)
    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()