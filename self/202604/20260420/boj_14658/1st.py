import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, M, L, K = map(int, input().split())
    stars = [tuple(map(int, input().split())) for _ in range(K)]
    
    ans = -float("inf")
    
    for sx, _ in stars:
        for _, sy in stars:
            tmp = 0
            for x, y in stars:
                if x >= sx and x <= sx+L and y >= sy and y <= sy+L: tmp += 1
            
            ans = max(ans, tmp)
            
    print(K-ans)
                
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()