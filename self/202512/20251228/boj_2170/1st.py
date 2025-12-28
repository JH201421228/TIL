import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    
    arr.sort()
    
    s, e = -float("inf"), -float("inf")
    
    ans = 0
    
    for idx in range(N):
        cur_s, cur_e = arr[idx]
        
        if cur_s > e:
            ans += e-s
            s, e = cur_s, cur_e
        
        else:
            e = max(e, cur_e)
            
    ans += e-s
    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()